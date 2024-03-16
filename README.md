# Serveless API AWS 
This repository demonstrates a simple project showcasing how to create an API in AWS using Terraform + FastAPI + Pytest + ECR + JWT + Lambda.

There is a freely accessible endpoint at "/", but all others require authentication using a bearer JWT.



## AWS Infrastructure

First of all, export your AWS credentials to your shell using:
```shell
export AWS_ACCESS_KEY_ID=""
export AWS_SECRET_ACCESS_KEY=""
export REGION=""
```

To automate the provision of the resources, [terraform](https://www.terraform.io/) is utilized. 

Typically, in a software development lifecycle, it is recommended to have separate `dev` and `prod` environments. To view available workspaces, use:

```shell
$ terraform workspace list
```
If a workspace has not been previously created, you can create a new one:
```shell
$ terraform workspace new dev
```

and then, select the desired workspace (in this case is dev):
```shell
$ terraform workspace select dev
```

### Creating
Use the following command to create an execution plan:
```shell
$ terraform plan -out="tfplan.out"
```
Finally, provision all coded infrastructure using:
```shell
$ terraform apply
```

### Updates in API (REDEPLOY)
The `plan` and `apply` commands of Terraform automatically verify updates in the api code and redeploy them as a new version to the ECR as the latest image to be used by Lambda. 


### Destroying
Be aware that using the command bellow, `ALL` resources created by terraform code will be destroyied:
```shell
$ terraform destroy
```

## Tests
To veriry if the api is working correctlly, use the following command:
```shell
$ pytest
```

Ensure that all dependencies located in [requirements.txt](api/requirements.txt) are installled.

## Docs
The documentation endpoin is freely accessible as well; no JWT authentication is necessary.
Access the application address using the endpoint `docs`, for example, `https:test.amazonaws.us-east-1/docs`, and observe how FastAPI generates an awesome Swagger Documentation on its own.


