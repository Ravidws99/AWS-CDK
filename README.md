# AWS-CDK-Cost-Saving-Lambdas

In this project, I utilized advanced AWS technologies to orchestrate a collection of automated Lambda Functions, targeting enhanced efficiency and cost management for AWS infrastructure. These functions range from managing EC2 and RDS instances, overseeing EBS snapshot maintenance, and Elastic IP Management to delivering a daily cost analysis via insights from Cost Explorer. Harnessing the AWS Python Cloud Development Kit (CDK) has enhanced the precision and efficiency of these deployments. Regular automation is facilitated through Amazon EventBridge, ensuring a proactive approach to resource management.

To further bolster the project's reliability and security, I incorporated tools like Snyk for Infrastructure as Code (IaC) scans, Bandit for Lambda security checks, and Pylint for maintaining code quality. The combination of CodePipeline and CodeCommit ensures seamless updates, reflecting any code modifications for a holistic AWS resource management and expenditure oversight.


## Architecture Breakdown

The lambda pipeline is broken down into the architecture below:

![lambda](https://github.com/rjones18/Images/blob/main/Lambda-Save-Money%20(4).png)
