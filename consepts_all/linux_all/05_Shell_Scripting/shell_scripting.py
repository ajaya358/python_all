# Shell Scripting - Automate tasks with bash scripts

print("=== Shell Script Basics ===")
print("""
#!/bin/bash
# First line always: #!/bin/bash (shebang)
# Run: chmod +x script.sh && ./script.sh

# Variables
NAME="Ajay"
AGE=25
echo "Name: $NAME, Age: $AGE"

# User input
read -p "Enter your name: " USER_NAME
echo "Hello $USER_NAME"

# If/else
if [ $AGE -gt 18 ]; then
    echo "Adult"
elif [ $AGE -eq 18 ]; then
    echo "Just turned adult"
else
    echo "Minor"
fi

# Comparison operators
# -eq  equal          -ne  not equal
# -gt  greater than   -lt  less than
# -ge  >=             -le  <=
# ==   string equal   !=   string not equal
""")

print("=== Loops ===")
print("""
# For loop
for i in 1 2 3 4 5; do
    echo "Number: $i"
done

# For loop over files
for file in *.py; do
    echo "Processing: $file"
done

# While loop
count=0
while [ $count -lt 5 ]; do
    echo "Count: $count"
    count=$((count + 1))
done
""")

print("=== Functions ===")
print("""
greet() {
    local name=$1   # $1 = first argument
    echo "Hello, $name!"
}
greet "Ajay"
greet "Ravi"
""")

print("=== Practical Scripts ===")
print("""
# 1. Deploy script
#!/bin/bash
echo "Pulling latest code..."
git pull origin main
echo "Installing dependencies..."
pip install -r requirements.txt
echo "Restarting service..."
sudo systemctl restart myapp
echo "Deploy complete!"

# 2. Backup script
#!/bin/bash
DATE=$(date +%Y-%m-%d)
tar -czf backup_$DATE.tar.gz /var/www/myapp
echo "Backup created: backup_$DATE.tar.gz"

# 3. Check if service is running
#!/bin/bash
if systemctl is-active --quiet nginx; then
    echo "Nginx is running"
else
    echo "Nginx is down! Restarting..."
    sudo systemctl start nginx
fi
""")
