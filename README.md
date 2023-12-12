# lambda-project
Repository for my take home assignment for Jasper Health

* Terraform Cloud https://app.terraform.io
* Terraform Registry for Providers and Modules https://registry.terraform.io/
* VScode
* AWS Lambda
* AWS API Gateway

1. Create your Workspace on Terraform
2. Included access keys as secret variables within Terraform Cloud.
3. Create terraform files for infrastructure.
4. Create Python file for Lambda Function.
5. Finish up configuration details in main.tf
6. Configurations for Lambda, API Gateway...etc
7. terraform init
8. terraform apply
   


Issues:
* I had very little trouble using Terraform to create a Lambda function with the appropriate IAM roles. However things started to go sideways once I integrated the AWS API Gateway.
* Instead of showing my "Hello World" message on the api_gateway_URL, I kept getting a {"message":"Missing Authentication Token"} error.
* Troubleshooting of issue continued.
* With limited time to do this project, I decided to see if I could utilize the 403 error to show my "Hello World" message.This unfortunately did not work.
* Issues will require more research to fix.

