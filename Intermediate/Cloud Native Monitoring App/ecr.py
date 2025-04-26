import boto3

client = boto3.client('ecr-public', region_name='us-east-1')

response = client.create_repository(
    repositoryName='cloud-native-repo',
    catalogData={
        'description': 'Cloud Native Application Repository',
        'architectures': [
            'x86-64',
        ],
        'operatingSystems': [
            'Linux',
        ],
        'aboutText': 'This repository contains the Cloud Native Application',
        'usageText': 'Use this repository to deploy the Cloud Native Application'
    },
    tags=[
        {
            'Key': 'Devops',
            'Value': 'FirstProject'
        },
    ]
)

print(response)