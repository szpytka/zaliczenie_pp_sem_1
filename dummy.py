import datetime
import random
import subprocess

# Get the current date and time
now = datetime.datetime.now()

# Generate a list of dates for the past three months
dates = [(now - datetime.timedelta(days=i)).strftime("%Y-%m-%d") for i in range(90)]

# Loop through the dates and create a commit for each one
for date in dates:
    # Generate a random commit message
    message = "Update " + date + " " + str(random.randint(1, 1000))

    # Write the message to a file
    with open("message.txt", "w") as f:
        f.write(message)

    # Run the Git commands to add and commit the changes
    subprocess.call(["git", "add", "."])
    subprocess.call(["git", "commit", "-F", "message.txt", "--date", date])
    subprocess.call(["git", "push"])
