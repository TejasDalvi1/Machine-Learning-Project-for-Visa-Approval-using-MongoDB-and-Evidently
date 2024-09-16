
===============================================================================
# Machine-Learning-Project-for-Visa-Approval-using-MongoDB-and-Evidently
===============================================================================
## Problem Statement

* OFLC processes job certification applications for employers bringing foreign workers to the U.S.
* Due to a high volume of applications last year, OFLC needs a machine learning model to shortlist visa applicants based on historical data.

## Project Goal:

* Build a classification model to predict visa approval based on the dataset.
* Use the model to recommend whether an applicant's visa should be certified or denied based on influential criteria.
===============================================================================

## Tech stack (libraries and tools) :
        (1)Python
        (2)scikit-learn
        (3)Mongo DB
        (4)Evidently
        (5)Docker
        (6)AWS:S3,EC2,ECR
        
===============================================================================
## To run :

```bash
conda create -n visa_approval python=3.8 -y
```

```bash
conda activate visa_approval
```

```bash
pip install -r requirements.txt
```
### Set the environment variables (inside OS system properties)
```bash
MONGODB_URL="mongodb+srv://<username>:<password>...."

AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>

AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>
```
```bash
python app.py
```
===============================================================================
## CICD on AWS using Github Actions
Here, we'll (A) Build docker image of the source code,
            (B) Push the image to AWS ECR,
            (C) Launch EC2,
            (D) Pull image from ECR in EC2,
            (E) Launch the docker image in EC2.

Follow the steps given below.         
(1) Login to AWS console.
(2) Create IAM user (with following policies)
    (a) AmazonEC2ContainerRegistryFullAccess
    (b) AmazonEC2FullAccess
    (c) AmazonS3FullAccess
(3) Create ECR repo to store docker image
    (Save URI. eg: 590184080569.dkr.ecr.us-east-1.amazonaws.com/visarepo)
(4) Create EC2 machine (Ubuntu,t2.large,storage:30GB)
(5) Open EC2 and Install docker (run the commands given below).
        sudo apt-get update -y #this is optional
        sudo apt-get upgrade #this is optional
        curl -fsSL https://get.docker.com -o get-docker.sh
        sudo sh get-docker.sh
        sudo usermod -aG docker ubuntu
        newgrp docker
(6) Configure EC2 as self-hosted runner on github.
        Settings(of project repo)-> Actions-> Runners-> New self-hosted runner-> choose os(Ubuntu)-> Run the commands sequentially
(7) Setup Secrets and variables (Inside settings of project repo).
        (a) AWS_ACCESS_KEY_ID,
        (b) AWS_SECRET_ACCESS_KEY,
        (c) AWS_DEFAULT_REGION,
        (d) ECR_REPO (name of repository eg. visarepo)
===============================================================================