To handle your JSON structure where the status field can be either a string or a dictionary, you can create a Python class with logic to handle this dynamic field. Here's how you can define the structure and parse the data into objects.


---

JSON Structure Example

Here’s an example JSON block based on your description:

[
  {
    "severity": "high",
    "time": "2024-11-23T10:00:00Z",
    "message": {
      "action": "Login",
      "source": "System",
      "status": "Success"
    }
  },
  {
    "severity": "low",
    "time": "2024-11-23T11:00:00Z",
    "message": {
      "action": "File Upload",
      "source": "User",
      "status": {
        "code": 200,
        "description": "File uploaded successfully"
      }
    }
  }
]


---

Python Classes to Represent the Data

You can define three classes: one for the entire JSON block (LogBlock), one for the message field (Message), and a wrapper for handling the optional status field.

class Message:
    def __init__(self, action, source, status):
        self.action = action
        self.source = source
        self.status = status

    def __repr__(self):
        return f"Message(action='{self.action}', source='{self.source}', status={self.status})"


class LogBlock:
    def __init__(self, severity, time, message):
        self.severity = severity
        self.time = time
        self.message = Message(
            action=message["action"],
            source=message["source"],
            status=message["status"]
        )

    def __repr__(self):
        return f"LogBlock(severity='{self.severity}', time='{self.time}', message={self.message})"


---

Parsing the JSON

Here’s how you can parse the JSON into LogBlock objects:

import json

# Load JSON data from a file
with open("data.json", "r") as file:
    json_data = json.load(file)

# Convert each JSON block into a LogBlock object
log_blocks = [LogBlock(block["severity"], block["time"], block["message"]) for block in json_data]

# Example usage
for log in log_blocks:
    print(log)

# Accessing specific properties
print(log_blocks[0].message.action)  # Output: Login
print(log_blocks[1].message.status)  # Output: {'code': 200, 'description': 'File uploaded successfully'}


---

Output

LogBlock(severity='high', time='2024-11-23T10:00:00Z', message=Message(action='Login', source='System', status='Success'))
LogBlock(severity='low', time='2024-11-23T11:00:00Z', message=Message(action='File Upload', source='User', status={'code': 200, 'description': 'File uploaded successfully'}))

Login
{'code': 200, 'description': 'File uploaded successfully'}


---

Handling the Dynamic status Field

In the Message class, the status field can handle both strings and dictionaries because Python allows dynamic typing. No special handling is required unless you want to add methods for specific cases.

For example, you can add a helper method to handle different status types:

class Message:
    def __init__(self, action, source, status):
        self.action = action
        self.source = source
        self.status = status

    def get_status_code(self):
        """Return the status code if status is a dictionary, else None."""
        return self.status.get("code") if isinstance(self.status, dict) else None

    def __repr__(self):
        return f"Message(action='{self.action}', source='{self.source}', status={self.status})"

Usage:

print(log_blocks[1].message.get_status_code())  # Output: 200


---

Advantages of This Approach

1. Object-Oriented: Encapsulates related data and logic within classes.


2. Flexibility: Handles fields like status that can have multiple data types.


3. Maintainability: Easy to add more fields or methods for additional functionality.


4. Readability: Accessing properties like log_blocks[0].message.action is intuitive.



Let me know if you’d like to extend this example further!

