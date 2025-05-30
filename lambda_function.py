# Adoring Fan Morning Slack Bot — Scheduled Version
# ------------------------------------------------
# A simple Slack bot that posts over-the-top, Adoring Fan–style morning messages
# at 9:00 AM UK time via an incoming webhook and AWS EventBridge Scheduler.
# Messages are written in the voice of Oblivion’s Adoring Fan to celebrate
# the recipient’s daily wake-up and login. 
#
# Built with AWS Lambda (Python 3.12), urllib3 & AWS EventBridge Scheduler
# Requires `messages.py` for your adoring messages list and SLACK_WEBHOOK_URL
# in environment variables. Schedule is fully customizable for any time or cadence.
#
# Author: Cameron Livingstone
# github.com/clive-jpg | 2025


from messages import messages
import os
import json
import random 
import urllib3

# Webhook URL for Slack pulls from environment variable
SLACK_WEBHOOK_URL = os.environ['SLACK_WEBHOOK_URL']

# Lambda function to trigger
def lambda_handler(event, context):
    
    # Randomly select a message from the predefined list
    payload = {
        "text": random.choice(messages),
}

# Send the message to Slack using the webhook URL
    http = urllib3.PoolManager()
    response = http.request(
        'POST',
        SLACK_WEBHOOK_URL,
        body=json.dumps(payload),
        headers={'Content-Type': 'application/json'}
    )
    
    # Return the response status and sent message
    return {
        "statusCode": response.status,
        "body": json.dumps({
            "sent_message": payload["text"],
            "slack_status": response.status
        })
}
