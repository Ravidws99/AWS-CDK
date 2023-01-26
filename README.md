# AWS-CDK-EC2-Shutdown-Lambda

In this project deployed a Lambda Function using the AWS Python CDK, CodePipeline, and CodeCommit. The Lambda Function checks for the existng active ec2 instances in each one of the regions for my account and cuts them off. I also added the Eventbrdge rule that triggers the lambda everyday.

## Architecture Breakdown

The lambda pipeline is broken down into the architecture below:

![lambda](https://github.com/rjones18/Images/blob/main/Lambda-Pipeline-Diagram.png)
