from constructs import Construct
import aws_cdk as cdk
from aws_cdk import (
    Duration,
    Stack,
    aws_lambda as _lambda,
    aws_iam as iam,
    aws_events as events,
    aws_events_targets as targets,
)


class CdkWorkshopStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        
        # Create IAM Role for Lambda to Assume
        role = iam.Role(self, "Role",
        assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
        role_name = "Lambda-EC2-Shutdown-Role"
    )
        # Attaching Permissions to Role
        role.attach_inline_policy(iam.Policy(self, "lambda-ec2-shutdown-policy",
        statements=[iam.PolicyStatement(
            actions=["ec2:StopInstances","ec2:DescribeInstances","ec2:DescribeInstanceStatus","ec2:DescribeRegions"],
            resources=['*']
            )]
        ))

        # Defines an AWS Lambda Resource
        my_lambda = _lambda.Function(
            self, 'HelloHandler',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.from_asset('lambda'),
            handler='hello.handler',
            role = role,
            timeout=cdk.Duration.minutes(3)
        )

        # Adding Event Bridge Rule
        rule = events.Rule(self, "Rule",
        schedule=events.Schedule.cron(minute="30", hour="20")
    )
        rule.add_target(targets.LambdaFunction(my_lambda))

