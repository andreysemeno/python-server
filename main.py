from fastapi import FastAPI
from dotenv import load_dotenv
import os

CONST_VER = "1.0"
hostname = os.uname().nodename  # Fixed method call and variable name

load_dotenv()
pywebd_message = os.environ.get('PYWEBD_MESSAGE', 'Default message')  # Added default value

app = FastAPI()

@app.get("/")
async def my_host():
    return {"data": f"{pywebd_message} from {hostname} app{CONST_VER}"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)  # Fixed indentation