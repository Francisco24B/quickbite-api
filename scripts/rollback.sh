
#!/bin/bash
APP_NAME=quickbite
PREVIOUS_VERSION=$1

docker stop $APP_NAME || true
docker rm $APP_NAME || true
docker run -d -p 80:8000 --name $APP_NAME $DOCKER_USER/quickbite-api:$PREVIOUS_VERSION
