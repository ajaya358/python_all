# Azure Blob Storage - Store files, images, backups
# Like AWS S3 — object storage
# pip install azure-storage-blob azure-identity

print("=== Blob Storage Concepts ===")
concepts = {
    "Storage Account": "Top-level container for all Azure storage services",
    "Container":       "Like S3 bucket — group of blobs",
    "Blob":            "A file stored in Azure (Block, Append, Page)",
    "Block Blob":      "Regular files — images, videos, documents",
    "Append Blob":     "Log files — can only append data",
    "Page Blob":       "VM disk files — random read/write",
    "Access Tier":     "Hot (frequent), Cool (infrequent), Archive (rare)",
    "SAS Token":       "Shared Access Signature — temporary URL with permissions",
}
for k, v in concepts.items():
    print(f"  {k:18}: {v}")

print("\n=== Blob Storage Operations ===")
print("""
from azure.storage.blob import BlobServiceClient, BlobClient
from azure.identity import DefaultAzureCredential

# Connect with connection string
conn_str = "DefaultEndpointsProtocol=https;AccountName=myaccount;AccountKey=mykey;..."
service_client = BlobServiceClient.from_connection_string(conn_str)

# Or with managed identity (recommended in production)
# credential = DefaultAzureCredential()
# service_client = BlobServiceClient(account_url="https://myaccount.blob.core.windows.net", credential=credential)

# Create container
container_client = service_client.create_container("my-container")

# Upload file
blob_client = service_client.get_blob_client(container="my-container", blob="folder/file.txt")
with open("local_file.txt", "rb") as f:
    blob_client.upload_blob(f, overwrite=True)

# Upload from string/bytes
blob_client.upload_blob(b"Hello Azure!", overwrite=True)

# Download file
with open("downloaded.txt", "wb") as f:
    data = blob_client.download_blob()
    f.write(data.readall())

# List blobs
container_client = service_client.get_container_client("my-container")
for blob in container_client.list_blobs():
    print(blob.name, blob.size)

# Delete blob
blob_client.delete_blob()

# Generate SAS URL (temporary access)
from azure.storage.blob import generate_blob_sas, BlobSasPermissions
from datetime import datetime, timedelta

sas_token = generate_blob_sas(
    account_name="myaccount",
    container_name="my-container",
    blob_name="file.txt",
    account_key="mykey",
    permission=BlobSasPermissions(read=True),
    expiry=datetime.utcnow() + timedelta(hours=1)
)
url = f"https://myaccount.blob.core.windows.net/my-container/file.txt?{sas_token}"
print(url)
""")

print("=== FastAPI File Upload to Azure Blob ===")
print("""
from fastapi import FastAPI, UploadFile
from azure.storage.blob import BlobServiceClient
import uuid

app = FastAPI()
service_client = BlobServiceClient.from_connection_string("your-connection-string")

@app.post("/upload")
async def upload(file: UploadFile):
    blob_name = f"uploads/{uuid.uuid4()}/{file.filename}"
    blob_client = service_client.get_blob_client(container="my-container", blob=blob_name)
    blob_client.upload_blob(await file.read(), overwrite=True)
    return {"blob": blob_name, "url": blob_client.url}
""")
