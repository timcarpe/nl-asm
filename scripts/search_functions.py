import requests
import json
import os
from urllib.parse import urlencode
from dotenv import load_dotenv
from gpt_functions import get_gpt_response_content
from logging_functions import log_message

# Load variables from .env file
load_dotenv()

google_api_key = os.getenv('GOOGLE_API_KEY')
cx = os.getenv('GOOGLE_CX')

def get_search_result(query):
    
    information = ""

    # Try to get the information from DuckDuckGo
    information = get_duckduckgo_info(query)

    # If we found information, return it
    if information != "":
        return information
    
    # Try to get the information from Google
    information = get_google_info(query)

    # If we found information, return it
    if information != "":
        return information
    
    #Temporary check so we can query LLM from main.py. In the future search will be more robust.
    return ""
    
    
def get_duckduckgo_info(query):

    sanitized_query = urlencode({'q': query})
    # Santize query
    q = sanitized_query

    url = f"https://api.duckduckgo.com/?{q}&format=json"

    log_message(">> DDG URL: " + url + "\n")

    response = requests.get(url)

    data = json.loads(response.content.decode('utf-8'))

    log_message(">> DDG data: " + json.dumps(data, indent=4) + "\n")

    if data['AbstractText'] != "":
        log_message(">> Found the following DDG AbstractText: " + data['AbstractText'] + "for query " + query + "\n")
        return data['AbstractText']
    elif data['Answer'] != "":
        log_message(">> Found the following DDG Answer: " + data['Answer'] + "for query " + query + "\n")
        return data['Answer']
    elif 'RelatedTopics' in data and data['RelatedTopics']:
        if data['RelatedTopics'][0]['Text'] != "":
            log_message(">> Found the following DDG RelatedTopics: " + data['RelatedTopics'][0]['Text'] + "for query " + query + "\n")
            return data['RelatedTopics'][0]['Text']
    else:
        log_message(">> No DDG data found for query: " + query + "\n")
        return ""

def get_google_info(query):
 

    url = f"https://www.googleapis.com/customsearch/v1?key={google_api_key}&cx={cx}&q={query}&num=1"

    log_message(">> Google URL: " + url + "\n")

    response = requests.get(url)

    data = json.loads(response.content.decode('utf-8'))

    log_message(">> Google data: " + json.dumps(data, indent=4) + "\n")
    information = ""
    if 'items' in data and data['items']:
        if 'snippet' in data['items'][0]:
            log_message(">> Found the following Google snippet: " + data['items'][0]['snippet'] + " for query " + query + "\n")
            information += data['items'][0]['snippet']
        elif 'metatags' in data and data['metatags']:
            if 'og:description' in data['metatags'][0]:
                log_message(">> Found the following Google og:description: " + data['metatags'][0]['og:description'] + " for query " + query + "\n")
                information += data['metatags'][0]['og:description']
    else:
        log_message(">> No Google data found for query: " + query + "\n")
    return information

#TODO  In the future summarize the search result agains the original query using a summarize function and return that instead.
def summarize_important_text(text):
    return get_gpt_response_content("system", text)