# 

## Local Cluster Setup
```sh
minikube --memory 4096 --cpus 4 start
minikube status
kubectl cluster-info
minikube dashboard
```

## AWS Cluster Setup

## Azure Cluster Setup

```sh
# https://docs.microsoft.com/en-us/azure/aks/kubernetes-walkthrough
az group create \
    -n sql-demo \
    -l germanywestcentral

az aks create \
    -g sql-demo \
    -n sql-demo-cluster
    -c 2
    --generate-ssh-keys

az aks get-credentials \
    -g sql-demo
    -n sql-demo-cluster
```

## AWS Cluster Setup

```sh

eksctl create cluster -f eks.yml 
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/download/v0.3.6/components.yaml
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.0.0-beta8/aio/deploy/recommended.yaml
kubectl apply -f dashboard-rbac.yml
echo http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/#!/login
kubectl proxy
```


# Running and accessing a pod and related resources imperatively
```sh
# kubectl api-resources

kubectl run dbs --image mokari94/dbservice

kubectl describe pods

# Create the pod
kubectl run dbs --image mokari94/dbservice --env LICENSE_KEY=SCOTLAND --port 8000
kubectl describe pods

# Create the service
kubectl expose pod dbs --type=LoadBalancer --port 8000

# Open the connection
minikube service dbs --url
```

# Running a pod and related resources declaratively
```sh
kubectl apply -f dbservice.yml
minikube service dbs --url
curl http://127.0.0.1:60953/user/1
```

# Let's have the pod fail 
```sh
curl http://127.0.0.1:60953/user/1
curl http://127.0.0.1:60953/fail
curl http://127.0.0.1:60953/user/1

# Check the log and the number of restarts
```

# Deployments
```sh
kubectl delete -f dbservice.yml
kubectl apply -f dbservice-deployment.yml
```

# helm 

