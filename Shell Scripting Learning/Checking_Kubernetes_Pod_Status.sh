#!/bin/bash

# Check for all running pods
kubectl get pods --all-namespaces

# Describe pods if needed
kubectl describe pod <pod-name> --namespace <namespace>
