# AWS-CDK-Cost-Saving-Lambdas

In this project, I leveraged sophisticated AWS technologies to deploy three automated Lambda Functions that provide maintenance and cost notifications for my AWS infrastructure. These resources were defined and managed using the AWS Python Cloud Development Kit (CDK), enhancing the precision and efficiency of the process.

The first Lambda Function systematically scans all regions of my AWS account, identifying active EC2 instances. It then automatically stops these instances to reduce unnecessary resource consumption, thereby minimizing costs. To ensure consistent operation, I incorporated an Amazon EventBridge rule, triggering this Lambda Function at regular intervals.

The second Lambda Function mirrors the first, but focuses on identifying and stopping active RDS instances across all regions. This step further curtails unnecessary resource usage and cost. An Amazon EventBridge rule was also implemented to automate this process, guaranteeing routine maintenance of the RDS instances.

The third Lambda Function provides a daily cost analysis. By extracting data from the Cost Explorer, it calculates the current charges accrued and emails a daily summary of my AWS balance.

To guarantee seamless delivery and updates to these Lambda Functions, I employed CodePipeline and CodeCommit, which enabled automatic deployment of any modifications. This project represents a comprehensive approach to manage, control, and monitor AWS resource utilization and expenses.




## Architecture Breakdown

The lambda pipeline is broken down into the architecture below:

![lambda](https://github.com/rjones18/Images/blob/main/Lambda-Save-Money.png)
