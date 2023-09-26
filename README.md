# Drug Classification
This project is related to the Kegel challenge. In this project, the goal is to classify drugs. In this project, a decision tree was used to classify drugs, and by using it, we achieved high accuracy in drug classification.

## The requirements of this project:
>* python3.11
>* install requirement.txt

We have also prepared a Docker file for this implementation of this project, which is located in the link below.
>* https://drive.google.com/file/d/1kPh3wxno9pOS9c2MyIT0GbuZvjSWUVNL/view?usp=sharing



## Instructions for using the Docker file
```bash
# load docker image
docker load -i <docker_tar_file>

# run docker image in background
docker run -d -it <id_image>

# Show running Dockers
docker ps 

# Run docker container integrated
docker exec -it <container_id> /bin/bash

```

You can use the following commands to build the Docker image.
```bash
docker build .

# Run the built Docker image file in integrated
docker run -it <image-ID> /bin/bash

```