#!/bin/bash

# Install Docker
sudo apt-get update
sudo apt-get install -y docker.io

# Install Minikube
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube


# Install kubectl
sudo apt-get install -y apt-transport-https ca-certificates curl gnupg lsb-release
curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin/kubectl

# Start Minikube
minikube start --driver=docker

# Verify installation
kubectl version
