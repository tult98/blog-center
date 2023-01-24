import fire
from python_on_whales import docker

def dev(service_name):
#    Step 1: kill all container(s) of the service
#    Step 2: Run a container in interactive shell
    container_name = '_'.join(service_name.split('-'))
    try:
        if docker.container.exists(container_name):
            docker.container.remove([container_name], force=True)
        docker.compose.run(service=service_name, name=container_name, service_ports=True, tty=True, remove=True, command=["sh"])
    except Exception as e:
        print(e)

if __name__ == '__main__':
  fire.Fire(dev)