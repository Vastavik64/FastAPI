import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":

    '''
    It sets database variables such as HOST and PORT.
    '''
    HOST = os.getenv("DB_HOST")
    PORT = os.getenv("DB_PORT")
    uvicorn.run("app.app:app", host= HOST , port= int(PORT) , reload= True)