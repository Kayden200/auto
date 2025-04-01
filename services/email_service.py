import time
import requests

def get_temp_email():
    response = requests.get("https://kaiz-apis.gleeze.com/api/tempmail-create").json()
    return response["email"], response["token"]

def get_otp(token):
    time.sleep(10)  
    inbox = requests.get(f"https://kaiz-apis.gleeze.com/tempmail-inbox?token={token}").json()
    for mail in inbox:
        if "Facebook" in mail["from"]:
            return mail["otp"]
    return None
