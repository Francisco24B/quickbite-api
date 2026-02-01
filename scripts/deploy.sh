
#!/bin/bash
APP_NAME=quickbite
VERSION=$(cat VERSION)
IMAGE=$DOCKER_USER/quickbite-api:$VERSION

docker pull $IMAGE
docker stop $APP_NAME || true
docker rm $APP_NAME || true
docker run -d -p 80:8000 --name $APP_NAME $IMAGE
