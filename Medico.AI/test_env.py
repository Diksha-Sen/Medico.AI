import os
os.chdir("..")
from dotenv import load_dotenv
result = load_dotenv()
print("load_dotenv result:", result)
print("Current dir:", os.getcwd())
print(".env exists:", os.path.exists('.env'))
