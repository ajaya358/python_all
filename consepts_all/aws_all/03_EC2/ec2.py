# AWS EC2 - Elastic Compute Cloud
# Virtual servers in the cloud — run your FastAPI app here

print("=== EC2 Key Concepts ===")
concepts = {
    "Instance":       "A virtual server (like a computer in the cloud)",
    "AMI":            "Amazon Machine Image — OS template (Ubuntu, Amazon Linux)",
    "Instance Type":  "CPU + RAM size (t2.micro, t3.medium, c5.xlarge)",
    "Key Pair":       "SSH key to connect to your server",
    "Security Group": "Firewall rules — which ports are open",
    "Elastic IP":     "Fixed public IP address for your instance",
    "EBS Volume":     "Hard disk attached to instance",
    "Auto Scaling":   "Automatically add/remove instances based on traffic",
    "Load Balancer":  "Distribute traffic across multiple instances",
}
for k, v in concepts.items():
    print(f"  {k:18}: {v}")

print("\n=== Instance Types ===")
types = {
    "t2.micro":   "1 vCPU, 1GB RAM   — Free tier, dev/test",
    "t3.small":   "2 vCPU, 2GB RAM   — Small apps",
    "t3.medium":  "2 vCPU, 4GB RAM   — Medium apps",
    "t3.large":   "2 vCPU, 8GB RAM   — Production apps",
    "c5.xlarge":  "4 vCPU, 8GB RAM   — CPU intensive (ML inference)",
    "r5.large":   "2 vCPU, 16GB RAM  — Memory intensive (Redis, DB)",
}
for k, v in types.items():
    print(f"  {k:12}: {v}")

print("\n=== Deploy FastAPI on EC2 ===")
print("""
# 1. Launch Ubuntu EC2 instance (t3.small or higher)
# 2. Open ports: 22 (SSH), 80 (HTTP), 443 (HTTPS), 8000 (FastAPI)

# 3. SSH into server
ssh -i my-key.pem ubuntu@<EC2_PUBLIC_IP>

# 4. Install dependencies
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip python3-venv nginx -y

# 5. Clone your app
git clone https://github.com/yourname/myapp.git
cd myapp
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 6. Run with uvicorn
uvicorn main:app --host 0.0.0.0 --port 8000

# 7. Run as service (stays running after logout)
sudo nano /etc/systemd/system/myapp.service
# [Unit]
# Description=FastAPI App
# [Service]
# User=ubuntu
# WorkingDirectory=/home/ubuntu/myapp
# ExecStart=/home/ubuntu/myapp/venv/bin/uvicorn main:app --host 0.0.0.0 --port 8000
# Restart=always
# [Install]
# WantedBy=multi-user.target

sudo systemctl enable myapp
sudo systemctl start myapp

# 8. Nginx reverse proxy (port 80 → 8000)
sudo nano /etc/nginx/sites-available/myapp
# server {
#     listen 80;
#     server_name yourdomain.com;
#     location / {
#         proxy_pass http://127.0.0.1:8000;
#     }
# }
sudo ln -s /etc/nginx/sites-available/myapp /etc/nginx/sites-enabled/
sudo systemctl restart nginx
""")

print("=== EC2 with boto3 ===")
print("""
import boto3
ec2 = boto3.client('ec2', region_name='ap-south-1')

# List instances
response = ec2.describe_instances()
for r in response['Reservations']:
    for i in r['Instances']:
        print(i['InstanceId'], i['State']['Name'], i.get('PublicIpAddress'))

# Start/Stop instance
ec2.start_instances(InstanceIds=['i-1234567890abcdef0'])
ec2.stop_instances(InstanceIds=['i-1234567890abcdef0'])
""")
