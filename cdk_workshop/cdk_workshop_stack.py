from constructs import Construct
import aws_cdk as cdk
from aws_cdk import (
    Duration,
    Stack,
    aws_lambda as _lambda,
    aws_iam as iam,
    aws_events as events,
    aws_events_targets as targets,
    aws_sns as sns,
    aws_sns_subscriptions as subscriptions,
    aws_secretsmanager as sm
)


class CdkWorkshopStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        
        # Create IAM Role for Lambdas to Assume
        role1 = iam.Role(self, "Role1",
        assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
        role_name = "Lambda-EC2-Shutdown-Role"
    )

        role2 = iam.Role(self, "Role2",
        assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
        role_name = "Lambda-RDS-Shutdown-Role"
    )
        role3 = iam.Role(self, "Role3",
        assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
        role_name = "Lambda-Billing-Role"
    )
        role4 = iam.Role(self, "Role4",
        assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
        role_name = "Lambda-EBS-Snapshot-Role"
    )
        
        role5 = iam.Role(self, "Role5",
        assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
        role_name = "Lambda-Elastic-IP-Role"
    )
    
        # Attaching Permissions to Roles
        role1.attach_inline_policy(iam.Policy(self, "lambda-ec2-shutdown-policy",
        statements=[iam.PolicyStatement(
            actions=["ec2:StopInstances","ec2:DescribeInstances","ec2:DescribeInstanceStatus","ec2:DescribeRegions"],
            resources=['*']
            )]
        ))

        role2.attach_inline_policy(iam.Policy(self, "lambda-rds-shutdown-policy",
        statements=[iam.PolicyStatement(
            actions=["rds:DescribeDBInstances","rds:StopDBInstance"],
            resources=['*']
            )]
        ))

        role3.attach_inline_policy(iam.Policy(self, "lambda-billing-policy",
        statements=[iam.PolicyStatement(
            actions=["ce:*"],
            resources=['*']
            )]
        ))

        role4.attach_inline_policy(iam.Policy(self, "lambda-ebs-snapshot-policy",
        statements=[iam.PolicyStatement(
            actions=["ec2:DescribeImages", "ec2:DescribeSnapshots", "ec2:DeleteSnapshot"],
            resources=['*']
            )]
        ))

        role5.attach_inline_policy(iam.Policy(self, "lambda-elastic-ip-policy",
        statements=[iam.PolicyStatement(
            actions=["ec2:DescribeAddresses", "ec2:ReleaseAddress"],
            resources=['*']
            )]
        ))

        role3.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("AmazonSNSFullAccess"))
        
        # Create SNS Topic For Billing Lambda
        sns_topic = sns.Topic(self, "CloudBillingSNSTopic")
        email = "reggiej3939@gmail.com"
        sns_topic.add_subscription(subscriptions.EmailSubscription(email))

        # Defines an AWS Lambda Resource
        my_lambda = _lambda.Function(
            self, 'Ec2Handler',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.from_asset('lambda'),
            handler='ec2.handler',
            role = role1,
            timeout=cdk.Duration.minutes(3)
        )
        my_lambda2 = _lambda.Function(
            self, 'rdsHandler',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.from_asset('lambda'),
            handler='rds.handler',
            role = role2,
            timeout=cdk.Duration.minutes(3)
        )

        my_lambda3 = _lambda.Function(
            self, 'billingHandler',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.from_asset('lambda'),
            handler='billing.handler',
            role = role3,
            timeout=cdk.Duration.minutes(3)
        )
        
        my_lambda4 = _lambda.Function(
            self, 'ebsHandler',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.from_asset('lambda'),
            handler='ebs.handler',
            role = role4,
            timeout=cdk.Duration.minutes(3)
        )

        my_lambda5 = _lambda.Function(
            self, 'ipsHandler',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.from_asset('lambda'),
            handler='ips.handler',
            role = role5,
            timeout=cdk.Duration.minutes(3)
        )

        # Grant SNS permissions to Lambda
        sns_topic.grant_publish(my_lambda3)

        # Add environment variable to Lambda function
        my_lambda3.add_environment("SNS_TOPIC_ARN", sns_topic.topic_arn)

       
       # Adding Event Bridge Rule
        rule = events.Rule(self, "Rule",
        schedule=events.Schedule.cron(minute="30", hour="20")
    )
        rule2 = events.Rule(self, "Rule 2",
        schedule=events.Schedule.cron(minute="00", hour="09")
    )
        rule.add_target(targets.LambdaFunction(my_lambda))
        rule.add_target(targets.LambdaFunction(my_lambda2))
        rule2.add_target(targets.LambdaFunction(my_lambda3))
        rule.add_target(targets.LambdaFunction(my_lambda4))
        rule.add_target(targets.LambdaFunction(my_lambda5))

