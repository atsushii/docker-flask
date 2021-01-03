docker build -t atsushiiii/multi-server:latest -t atsushiiii/multi-server:$SHA -f flask-docker-travisci-ks8/Dockerfile.prod .

docker push atsushiiii/multi-server:latest
docker push atsushiiii/multi-server:$SHA

kubectl apply -f k8s
kubectl set image server-deployment server=atsushiiii/multi-server:$SHA
