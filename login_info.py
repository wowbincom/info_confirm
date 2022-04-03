#!/usr/bin/python3
from dotenv import load_dotenv
import os

#==================
load_dotenv()
print(os.getenv("PATH"))

PASSOWRD = os.getenv("PASSWORD")
EMAIL_ADDR = os.getenv("EMAIL_ADDR")

login_info = {
    'EMAIL_ADDR' : EMAIL_ADDR,
    'PASSWORD' : PASSOWRD
}

print(login_info)