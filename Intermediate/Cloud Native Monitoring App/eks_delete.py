from kubernetes import client, config

config.load_kube_config()

core_v1 = client.CoreV1Api()
apps_v1 = client.AppsV1Api()

try:
    # Delete Service
    core_v1.delete_namespaced_service(
        name="monitoring-service",
        namespace="default"
    )
    print("✅ 'monitoring-service' Service deleted.")

    # Delete Deployment
    apps_v1.delete_namespaced_deployment(
        name="monitoring-app",  # Deployment name
        namespace="default"
    )
    print("✅ 'monitoring-app' Deployment deleted.")
except client.rest.ApiException as e:
    print(f"❌ Error: {e.reason}")