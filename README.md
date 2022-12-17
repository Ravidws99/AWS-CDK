# AWS-Python-CDK-EC2-Shutdown-Lambda

In this project created a Lambda Funtion using the AWS Python CDK, CodePipeline, and CodeCommit. The Lambda Function checks for the existng active ec2 instances in each one of the regions for my account and them cuts off. I also added the Eventbrdge rule that triggers the lambda everyday.

## Architecture Breakdown

The lambda pipeline is broken down into the architecture below:

![lambda](https://github.com/rjones18/Images/blob/main/Lambda-Pipeline-Diagram.png)
