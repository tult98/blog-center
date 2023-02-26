#!/usr/bin/python3
import fire
from python_on_whales import docker

class Container():
    def dev(self, service_name):
    #    Step 1: kill all container(s) of the service
    #    Step 2: Run a container in interactive shell
        try:
            if docker.container.exists(service_name):
                docker.container.remove([service_name], force=True)
            docker.compose.run(service=service_name, name=service_name, service_ports=True, tty=True, remove=True, command=["sh"])
        except Exception as e:
            print(e)

if __name__ == '__main__':
  fire.Fire(Container)