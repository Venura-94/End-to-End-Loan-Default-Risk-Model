# End-to-End-Loan Default Risk Prediction 

Projects Target Audience - Empowering banks with critical insights into factors influencing loan defaults, predictive model aims to refine loan authorization processes and risk assessments.

### The model is still in researching phase (Data Preprocessing block and hyperparamter tuning)

![image](https://github.com/Venura-94/End-to-End-Loan-Default-Risk-Model/assets/137409412/31b5db88-a5e3-48c0-8f41-477829aa2753)

### Diagrams to Explain the Project's End-to-End Deployment (Pipeline Architecture & AWS Delpoyment Architecture)

![image](https://github.com/Venura-94/End-to-End-Loan-Default-Risk-Model/assets/137409412/4346e95f-51cf-4d23-a866-ee59fc6db7c5)


![AWS_CICD_EC2](https://github.com/Venura-94/End-to-End-Loan-Default-Risk-Model/assets/137409412/b1419411-3f3f-40ad-aa5d-934f5c0665d8)


This workflow enables  to automate the deployment of the application from  GitHub repository to an AWS EC2 instance via Docker images stored in ECR, using GitHub Actions as the orchestrator and a self-hosted runner on an EC2 instance.

# Workflow explained below step-by-step for ease of comprehension
## Folder WorkFlow

1. update config.yaml
2. update schema.yaml
3. update params.yaml
4. update the entity 
5. update the src config
6. update the components
7. update the pipeline
8. update the main.py
9. update the app.py

# Creating the environment and installing the requirements
### STEPS:


```bash
conda create -n mlproj python=3.8 -y 
```

```bash
conda activate mlproj
```


```bash
pip install -r requirements.txt
```

```bash
python app.py
```

# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

![AWS Dash Board Free Tier](https://github.com/Venura-94/End-to-End-Loan-Default-Risk-Model/assets/137409412/551bb047-b36b-436f-8bd3-434ee45dc2d9)

## 2. Create IAM user for deployment


![IAM User](https://github.com/Venura-94/End-to-End-Loan-Default-Risk-Model/assets/137409412/c4c1c122-73ef-4f0f-bd68-6c39df26bd4d)


	#with specific access

	1. EC2 access : virtual machine

	2. ECR: Elastic Container registry to save the docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code
![image](https://github.com/Venura-94/End-to-End-Loan-Default-Risk-Model/assets/137409412/46f20dd9-59db-4221-b70e-004991f4146a)

	2. Push the docker image to ECR
![Images to Registry](https://github.com/Venura-94/End-to-End-Loan-Default-Risk-Model/assets/137409412/1e65b57c-9de3-474b-8580-7ff1dd49c83f)

	3. Launch the EC2 
![EC2 dashboard](https://github.com/Venura-94/End-to-End-Loan-Default-Risk-Model/assets/137409412/8515a303-a61c-4d3b-aee2-93e3abfd4f34)



	4. Pull the image from ECR in EC2

	5. Lauch the docker image in EC2

![Port added](https://github.com/Venura-94/End-to-End-Loan-Default-Risk-Model/assets/137409412/3979cc0c-6c3c-4e2f-bd6b-86c3a00f0f1a)

### Prediction UI

![webapp](https://github.com/Venura-94/End-to-End-Loan-Default-Risk-Model/assets/137409412/1338b400-9152-4cf9-86b2-dd78242c0e84)


	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 169712768495.dkr.ecr.us-east-1.amazonaws.com/mlproject
![Elastic Container Registry](https://github.com/Venura-94/End-to-End-Loan-Default-Risk-Model/assets/137409412/3a1c806e-b819-467d-88c5-3bc72074171d)

	
## 4. Create EC2 machine (Ubuntu) 
![EC2 Instance](https://github.com/Venura-94/End-to-End-Loan-Default-Risk-Model/assets/137409412/f9020e2a-d9dd-454c-a762-05c2fa65971c)


## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker

# After Installing docker and completion of CI/CD_ EC2 CLI 

![EC2 CLI](https://github.com/Venura-94/End-to-End-Loan-Default-Risk-Model/assets/137409412/3b0e7731-b2c8-4ba8-8e85-4a12571fd9bb)

 
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one
![Runner](https://github.com/Venura-94/End-to-End-Loan-Default-Risk-Model/assets/137409412/74fca882-bc75-490d-a4fc-60904bd8f8ed)

![Selfhosted Runner](https://github.com/Venura-94/End-to-End-Loan-Default-Risk-Model/assets/137409412/49efc4bd-7387-46a4-b31c-ecd92ef2d006)

At the moment runner is offline i have removed the related instance from AWS

Completion of Github Workflows (CI/CD)

![Actions_All Workflows](https://github.com/Venura-94/End-to-End-Loan-Default-Risk-Model/assets/137409412/43b3c790-9cef-4d53-abe0-b05cb192dec7)
![Github actions workflow](https://github.com/Venura-94/End-to-End-Loan-Default-Risk-Model/assets/137409412/cfab58c0-0c5d-402b-a1ad-77248ad607f4)


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app

