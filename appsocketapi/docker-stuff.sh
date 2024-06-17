cd appsocketapi
docker build -t appsocketapi .

docker stop appsocketapi
docker rm appsocketapi

docker run -d -p 5080:80 --name appsocketapi appsocketapi

