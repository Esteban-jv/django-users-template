from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv("DJANGO_DATABASE_NAME"))