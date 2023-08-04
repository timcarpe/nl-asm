import wolframalpha
import os
from dotenv import load_dotenv
from logging_functions import log_message

# Load variables from .env file
load_dotenv()


app_id = os.getenv('WOLFRAM_APP_ID')
client = wolframalpha.Client(app_id)

def get_wolframalpha_result(query):
    information = ""

    log_message(">> WolframAlpha query: " + query + "\n")

    result = client.query(query)

    log_message(">> WolframAlpha result: " + str(result) + "\n")
    
    for pod in result.pods:
        information += pod.title + ": " + pod.text + "\n"
    
    return information