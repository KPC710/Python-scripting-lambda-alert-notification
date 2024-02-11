from kubernetes import client, config

def get_pods_info():
    try:
        config.load_kube_config()  # Load kubeconfig from default location
        v1 = client.CoreV1Api()
        pod_list = v1.list_pod_for_all_namespaces(watch=False)
        print("Pods in the cluster:")
        for pod in pod_list.items:
            print(f" - {pod.metadata.name} in {pod.metadata.namespace}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    get_pods_info()
