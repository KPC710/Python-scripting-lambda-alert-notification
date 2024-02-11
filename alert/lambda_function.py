# lambda_function.py

import json
from codebuild_handler import CodeBuildEvent
from slack_notifier import SlackNotifier


def lambda_handler(event, context):
    print("Received Event:")
    print(json.dumps(event))

    # Assuming the Slack webhook URL is passed as an environment variable
    slack_webhook_url = "YOUR_SLACK_WEBHOOK_URL"
    slack_notifier = SlackNotifier(slack_webhook_url)

    # Process CodeBuild events
    if event['source'] == 'aws.codebuild':
        codebuild_event = CodeBuildEvent(event)
        print("Processing CodeBuild Event:", codebuild_event)

        # Example: Send a simple notification to Slack
        message = f"CodeBuild {codebuild_event.project_name} {codebuild_event.build_status}"
        status_code = slack_notifier.send_message(message)

        print(f"Slack Notification Status Code: {status_code}")
    else:
        print("Unknown event source")

    return {
        'statusCode': 200,
        'body': json.dumps('Done')
    }

