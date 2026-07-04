# AWS Lambda - Serverless Functions
# Run code without managing servers — pay per execution

print("=== What is Lambda? ===")
concepts = {
    "Serverless":   "No server to manage — AWS handles infrastructure",
    "Function":     "Single Python function that handles one task",
    "Trigger":      "What starts the function (API Gateway, S3, SQS, schedule)",
    "Handler":      "Entry point function: def handler(event, context)",
    "Event":        "Input data passed to function (JSON)",
    "Context":      "Runtime info (timeout, memory, request ID)",
    "Cold Start":   "First invocation is slow (container spin-up)",
    "Warm Start":   "Subsequent calls are fast (container reused)",
    "Timeout":      "Max 15 minutes per execution",
    "Memory":       "128MB to 10GB — more memory = more CPU too",
}
for k, v in concepts.items():
    print(f"  {k:14}: {v}")

print("\n=== Lambda Handler Structure ===")
print("""
def handler(event, context):
    # event  = input data (dict)
    # context = runtime info

    print("Event:", event)
    print("Request ID:", context.aws_request_id)

    # Your logic here
    name = event.get('name', 'World')
    return {
        'statusCode': 200,
        'body': f'Hello {name}!'
    }
""")

print("=== Lambda with API Gateway ===")
print("""
# API Gateway → Lambda → Response
# Each route can be a separate Lambda function

def handler(event, context):
    method = event['httpMethod']
    path   = event['path']
    body   = event.get('body', '{}')

    if method == 'GET' and path == '/users':
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': '[{"id": 1, "name": "Ajay"}]'
        }

    return {'statusCode': 404, 'body': 'Not found'}
""")

print("=== Lambda Triggers ===")
triggers = {
    "API Gateway":  "HTTP request → Lambda → response (REST API)",
    "S3":           "File uploaded to S3 → Lambda processes it",
    "SQS":          "Message in queue → Lambda processes it",
    "CloudWatch":   "Scheduled (cron) → Lambda runs periodically",
    "DynamoDB":     "DB record changed → Lambda reacts",
    "SNS":          "Notification published → Lambda handles it",
}
for k, v in triggers.items():
    print(f"  {k:14}: {v}")

print("\n=== Deploy Lambda with Python ===")
print("""
# 1. Write handler in lambda_function.py
# 2. Zip with dependencies:
pip install requests -t ./package
cd package && zip -r ../deployment.zip .
cd .. && zip deployment.zip lambda_function.py

# 3. Upload via AWS CLI
aws lambda create-function \\
  --function-name my-function \\
  --runtime python3.11 \\
  --handler lambda_function.handler \\
  --zip-file fileb://deployment.zip \\
  --role arn:aws:iam::123456789:role/lambda-role

# 4. Invoke function
aws lambda invoke \\
  --function-name my-function \\
  --payload '{"name": "Ajay"}' \\
  response.json
""")

print("=== FastAPI on Lambda (Mangum) ===")
print("""
# pip install mangum
from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def root():
    return {"message": "FastAPI on Lambda!"}

# Lambda handler
handler = Mangum(app)
""")
