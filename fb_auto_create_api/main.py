from fastapi import FastAPI
from services.fb_creator import create_fb_account
from utils.random_generator import generate_random_password, generate_random_name
from services.email_service import get_temp_email, get_otp

app = FastAPI()

@app.post("/create_fb_account")
def api_create_fb_account():
    first_name, last_name = generate_random_name()
    password = generate_random_password()
    email, token = get_temp_email()
    
    status = create_fb_account(email, password, first_name, last_name)
    otp = get_otp(token)

    return {
        "email": email,
        "password": password,
        "otp": otp if otp else "OTP retrieval failed",
        "status": status
    }
