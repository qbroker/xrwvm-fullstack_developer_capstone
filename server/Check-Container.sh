#!/bin/sh

# Check for persisting sessions
# Remove: kubectl delete deployment dealership
echo "Check if there are kubernetes deployments"
kubectl get deployments

#Remove: ibmcloud cr image-rm us.icr.io/<your sn labs namespace>/dealership:latest && docker rmi us.icr.io/<your sn labs namespace>/dealership:latest
echo "Check for IBMcloud images"
ibmcloud cr images
