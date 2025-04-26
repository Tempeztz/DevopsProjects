from kubernetes import client, config

# Load kube config
config.load_kube_config()

# --- Existing Deployment Code ---
container = client.V1Container(
    name="monitoring-app",
    image="public.ecr.aws/l7q1j0d4/cloud-native-repo:latest",
    ports=[client.V1ContainerPort(container_port=5000)]
)

template = client.V1PodTemplateSpec(
    metadata=client.V1ObjectMeta(labels={"app": "monitoring-app"}),
    spec=client.V1PodSpec(containers=[container])
)

spec = client.V1DeploymentSpec(
    replicas=1,
    selector=client.V1LabelSelector(match_labels={"app": "monitoring-app"}),
    template=template
)

deployment = client.V1Deployment(
    api_version="apps/v1",
    kind="Deployment",
    metadata=client.V1ObjectMeta(name="monitoring-app"),
    spec=spec
)

apps_v1 = client.AppsV1Api()
apps_v1.create_namespaced_deployment(namespace="default", body=deployment)
print("✅ 'monitoring-app' Deployment created.")

# --- New Service Configuration ---
# Define the Service
service = client.V1Service(
    api_version="v1",
    kind="Service",
    metadata=client.V1ObjectMeta(name="monitoring-service"),
    spec=client.V1ServiceSpec(
        selector={"app": "monitoring-app"},  # Matches Deployment's pods
        ports=[client.V1ServicePort(
            port=5000,        # Service port (external access)
            target_port=5000  # Pod port (matches container_port)
        )],
        type="ClusterIP"    # Options: ClusterIP, NodePort, LoadBalancer
    )
)

# Create the Service
core_v1 = client.CoreV1Api()
core_v1.create_namespaced_service(namespace="default", body=service)
print("✅ 'monitoring-service' Service created.")