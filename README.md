# AWS-CDK-EC2-Shutdown-Lambda

In this project, I utilized a suite of advanced AWS technologies to deploy a Lambda Function that performs automated maintenance on my AWS infrastructure. I utilized the AWS Python Cloud Development Kit (CDK) to define the AWS resources needed to host the Lambda Function. To ensure continuous delivery, I leveraged CodePipeline and CodeCommit to automatically deploy any updates to the Lambda Function.

The Lambda Function itself is designed to check for any existing active EC2 instances in each region of my AWS account and stops them. This functionality helps prevent unnecessary resource usage and minimizes costs associated with running inactive EC2 instances. To automate the process, I also added an Amazon EventBridge rule to trigger the Lambda Function at a specified time interval, ensuring regular maintenance of the EC2 instances.

By integrating this modern technology stack with AWS's powerful cloud computing infrastructure, I was able to deploy an efficient and cost-effective solution for automated maintenance of my AWS resources.




## Architecture Breakdown

The lambda pipeline is broken down into the architecture below:

![lambda](https://github.com/rjones18/Images/blob/main/Lambda-Pipeline-Diagram.png)
