from constructs import Construct
from aws_cdk.aws_secretsmanager import Secret
from aws_cdk import (
    Stack,
    aws_codecommit as codecommit,
    pipelines as pipelines,
    aws_codebuild,
    aws_secretsmanager,
    aws_codepipeline_actions,
    aws_codepipeline as codepipeline,
    aws_iam,
    aws_ssm
)
from cdk_workshop.pipeline_stage import WorkshopPipelineStage

class WorkshopPipelineStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Creates a CodeCommit repository called 'WorkshopRepo'
        repo = codecommit.Repository(
            self, "WorkshopRepo", repository_name="Cost-Saving-Lambda-Functions-Pipeline"
        )

        secret_name = "snyk-key"
        snyk_secret = Secret.from_secret_name_v2(self, "ExistingSecretByName", secret_name)
        
        pipeline = pipelines.CodePipeline(
            self,
            "Pipeline",
            synth=pipelines.ShellStep(
                "Synth-and-Security-Check",
                input=pipelines.CodePipelineSource.code_commit(repo, "master"),
                commands=[
                    "npm install -g aws-cdk",  # Installs the cdk cli on Codebuild
                    'npm install -g snyk',
                    "pip install -r requirements.txt",
                    'snyk auth $SNYK_TOKEN',
                    "cdk synth",
                    'snyk iac test --report || echo "Snyk found vulnerabilities!"',
                    "bandit -r ./lambda",
                    "pylint ./lambda || true"

                ],
                    env={
                        'SNYK_TOKEN': snyk_secret.secret_value.unsafe_unwrap()
                    }
            ),
        )

        deploy = WorkshopPipelineStage(self, "Deploy")
        deploy_stage = pipeline.add_stage(deploy)
