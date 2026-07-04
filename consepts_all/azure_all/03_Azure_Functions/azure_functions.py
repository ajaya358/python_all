# Azure Functions - Serverless compute (like AWS Lambda)
# pip install azure-functions

print("=== Azure Functions Concepts ===")
concepts = {
    "Function App":   "Container that hosts one or more functions",
    "Trigger":        "What starts the function (HTTP, Timer, Queue, Blob)",
    "Binding":        "Connect to other services (input/output) without code",
    "Consumption Plan":"Pay per execution, auto-scale to zero",
    "Premium Plan":   "Pre-warmed instances, no cold start",
    "Durable Functions":"Stateful workflows — chain functions together",
}
for k, v in concepts.items():
    print(f"  {k:18}: {v}")

print("\n=== HTTP Trigger Function ===")
print("""
# function_app.py
import azure.functions as func
import json

app = func.FunctionApp()

@app.route(route="hello", methods=["GET", "POST"])
def hello(req: func.HttpRequest) -> func.HttpResponse:
    name = req.params.get('name') or req.get_json().get('name', 'World')
    return func.HttpResponse(
        json.dumps({"message": f"Hello {name}!"}),
        mimetype="application/json",
        status_code=200
    )
""")

print("=== Timer Trigger (Scheduled) ===")
print("""
@app.timer_trigger(schedule="0 */5 * * * *", arg_name="timer")  # every 5 minutes
def scheduled_job(timer: func.TimerRequest) -> None:
    print("Running scheduled job...")
    # cleanup, sync data, send reports, etc.
""")

print("=== Blob Trigger (React to file upload) ===")
print("""
@app.blob_trigger(arg_name="blob", path="uploads/{name}", connection="AzureWebJobsStorage")
def process_upload(blob: func.InputStream) -> None:
    print(f"Processing blob: {blob.name}, size: {blob.length}")
    data = blob.read()
    # process image, parse CSV, etc.
""")

print("=== Queue Trigger (Process messages) ===")
print("""
@app.queue_trigger(arg_name="msg", queue_name="my-queue", connection="AzureWebJobsStorage")
def process_queue(msg: func.QueueMessage) -> None:
    data = msg.get_json()
    print(f"Processing message: {data}")
""")

print("\n=== Deploy Azure Function ===")
print("""
# Install Azure Functions Core Tools
npm install -g azure-functions-core-tools@4

# Create new function project
func init myapp --python
cd myapp
func new --name hello --template "HTTP trigger"

# Run locally
func start

# Deploy to Azure
az login
func azure functionapp publish my-function-app
""")
