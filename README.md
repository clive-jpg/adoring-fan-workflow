# Adoring Fan Slack Bot

A scheduled Slack bot that posts over-the-top, Adoring Fan–style morning messages. Written in the shrill, giddy voice of Oblivion’s Adoring Fan, it transforms your day into theatrical spectacle.


![Adoring Fan Workflow Screenshot](assets/adoring-fan-dm-example.png)

---

## 🚀 How I Built It

1. **HTTP & Slack Workflows**  
   I started by exploring Slack’s simple Workflow Builder and realized you can trigger a step based on an incoming webhook, pull a variable from the payload, and inject it into a message.

2. **AWS Lambda**  
   To make it fully serverless and reliable, I moved the logic into a Python (3.12) Lambda function that picks a random message from `messages.py` and posts it via `urllib3` to the Slack webhook.

3. **EventBridge Scheduler**  
   Slack workflows don’t support scheduled posts, so I wired up an AWS EventBridge Scheduler rule (cron in UTC) to invoke the Lambda at 09:00 GMT every day. The EventBridgge itself double-checks Europe/London time so it handles BST/GMT shifts gracefully.

4. **Customization**  
   It’s easy to adapt this for other times, channels, or specific users—just update the AWS EventBridge cron expression for custom time, change the message list in the code and define the steps on who should recieve the message

---



