import boto3
import datetime
import os

def handler(event, context):
    region = os.environ.get('AWS_REGION', 'us-east-1')
    ce = boto3.client('ce', region_name=region)
    sns = boto3.client("sns")
    sns_topic_arn = os.environ["SNS_TOPIC_ARN"]

    today = datetime.datetime.now()
    start_date = today.strftime("%Y-%m-01")
    end_date = today.strftime("%Y-%m-%d")

    response = ce.get_cost_and_usage(
        TimePeriod={
            'Start': start_date,
            'End': end_date
        },
        Granularity='MONTHLY',
        Metrics=['BlendedCost']
    )

    money = response['ResultsByTime'][0]['Total']['BlendedCost']['Amount']
    cost = round(float(money), 2)
    currency = response['ResultsByTime'][0]['Total']['BlendedCost']['Unit']

    sns.publish(
        TopicArn=sns_topic_arn,
        Subject=f"AWS Bill for {today}",
        Message=f"Your Current AWS Charges: {cost} {currency}"
    )
    return {
        'statusCode': 200,
        'body': f"Current AWS charges: {cost} {currency}"
    }