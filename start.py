import os

docker_rabbitmq_img = "docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.12-management"
os.system(docker_rabbitmq_img)
