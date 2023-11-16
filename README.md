# Plant Disease Detection

## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py


## Dataset

* You can use any dataset (including the Kaggle dataset) that is supported by [opendatasets] (https://github.com/JovianHQ/opendatasets). Just place the URL of the dataset in `config/config.yaml/data_ingestion/source_URL` 
* If you want to use your custom dataset, just place it inside the `artifacts/data_ingestion/dataset` folder or any other custom folder that you have to mention in `config/config.yaml/data_ingestion/dataset_dir` 

## Steps to run

### STEP 00 : Clone the repository

```bash
https://github.com/utpal108/plant-disease-detection
```
### STEP 01 : Create a virtial environment after opening the repository

Using Anaconda Virtual Environments

```bash
conda create -n venv python=3.10 -y
conda activate venv
```
Or for Linux operating system, you can use that

```bash
python3.10 -m venv venv
source venv/bin/activate
```


### STEP 02 : install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,open up your local host with a port like that.
`http://localhost:8080`



## AWS-CICD-Deployment-with-Github-Actions

### STEP 00 : Login to AWS console.

### STEP 01 : Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
### STEP 02 : Create ECR repo to store/save docker image
    - Save the URI: 681776806933.dkr.ecr.us-east-2.amazonaws.com/plant-disease-detection

	
### STEP 03 : Create EC2 machine (Ubuntu) 

### STEP 04 : Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
### STEP 05 : Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


### STEP 06 : Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-2

    AWS_ECR_LOGIN_URI = demo>>  681776806933.dkr.ecr.us-east-2.amazonaws.com

    ECR_REPOSITORY_NAME = plant-disease-detection