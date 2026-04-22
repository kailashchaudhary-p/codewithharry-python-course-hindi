import os

path = "/"   # change this to your directory path

try:
    for name in os.listdir(path):
        print(name)
except FileNotFoundError:
    print("Directory not found:", path)
except PermissionError:
    print("No permission to access:", path)
