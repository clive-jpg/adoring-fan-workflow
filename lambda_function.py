import json
import random 
import urllib3


messages = [
'By Azura! By Azura Its you',
'You dont write bugs, you write features',
'You are a true hero of the realm',
'You are the chosen one',
'You are the one who will save us all', 
]

def lambda_handler(event, context):
    
    payload = {
        "text": random.choice(messages),
}

    http = urllib3.PoolManager()
    response = http.request(
        'POST',
        SLACK_WEBHOOK_URL,
        body=json.dumps(payload),
        headers={'Content-Type': 'application/json'}
    )
    
    return {
        "statusCode": response.status,
        "body": json.dumps({
            "sent_message": payload["text"],
            "slack_status": response.status
        })
}