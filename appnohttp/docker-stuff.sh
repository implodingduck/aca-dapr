docker build -t appnohttp .

docker stop appnohttp
docker rm appnohttp

docker run --name appnohttp appnohttp
