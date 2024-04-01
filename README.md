# End-to-end-Loan Default Risk Prediction (Random Forest Classifier Problem)
### Currently running parameters and model is still in researching phase (Preprocessing block and hyperparamter tuning)
![image](https://github.com/Venura-94/End-to-End-Loan-Default-Risk-Model/assets/137409412/e280a874-0e16-4090-9c02-aaa8b2629753)


## Folder WorkFlow

1. update config.yaml
2. update schema.yaml
3. update params.yaml
4. update the entity 
5. update the configuration manager in src config
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

```bash
Now open up your local host 0.0.0.0:8080
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

	4. Pull the image from ECR in EC2

	5. Lauch the docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 169712768495.dkr.ecr.us-east-1.amazonaws.com/mlproject

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
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

