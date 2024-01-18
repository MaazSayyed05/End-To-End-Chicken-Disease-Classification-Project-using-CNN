# End-To-End-Chicken-Disease-Classification-Project-using-CNN


### dataset url: https://www.kaggle.com/datasets/muhammadmaazsayyed/chicken-disease-dataset

## Workflows

1. Update config.yaml file
2. Update secrets.yaml [optional]
3. Update params.yaml
4. Update entity 
5. Update configuration maanger in src
6. Update components
7. Update pipeline
8. Update main.py
9. Update dvc.yaml file




# AZURE-CICD-Deployment-with-Github-Actions

## Save pass:

s3cEZKH5yytiVnJ3h+eI3qhhzf9q1vNwEi6+q+WGdd+ACRCZ7JD6


## Run from terminal:

docker build -t chickenapp.azurecr.io/chicken:latest .

docker login chickenapp.azurecr.io

docker push chickenapp.azurecr.io/chicken:latest


## Deployment Steps:

1. Build the Docker image of the Source Code
2. Push the Docker image to Container Registry
3. Launch the Web App Server in Azure 
4. Pull the Docker image from the container registry to Web App server and run 
