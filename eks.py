from kubernetes import client, config

config.load_kube_config()

api_client = client.ApiClient()

# deployment
deployment = client.V1Deployment(
    metadata=client.V1ObjectMeta(name="monitoring-app", namespace="default"),
    spec=client.V1DeploymentSpec(
        replicas=1,
        selector=client.V1LabelSelector(match_labels={"app": "monitoring-app"}),
        template=client.V1PodTemplateSpec(
            metadata=client.V1ObjectMeta(labels={"app": "monitoring-app"}),
            spec=client.V1PodSpec(
                containers=[
                    client.V1Container(
                        name="monitoring-app",
                        image="327207168124.dkr.ecr.us-east-1.amazonaws.com/cloud-monitoring-app:latest",
                        ports=[client.V1ContainerPort(container_port=5000)],
                    )
                ]
            ),
        ),
    ),
)

# create deployment
api_instance = client.AppsV1Api(api_client)
api_response = api_instance.create_namespaced_deployment(
    body=deployment,
    namespace="default",
)

# create service
service = client.V1Service(
    metadata=client.V1ObjectMeta(name="monitoring-app", namespace="default"),
    spec=client.V1ServiceSpec(
        selector={"app": "monitoring-app"},
        ports=[client.V1ServicePort(port=80, target_port=5000)],
        type="LoadBalancer",
    ),
)

api_instance = client.CoreV1Api(api_client)
api_instance.create_namespaced_service(
    body=service,
    namespace="default",
)
