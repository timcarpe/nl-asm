# Introduction

This is a program that I created because I wanted to see if ChatGPT could write code for a new programming language using documentation.

Once I was I surprised by the ability to write the code I created this program to execute the code.

ChatGPT will write its own program for your request. For example it may search or query itself for pros and then cons and assign them to a memory address. It will then use those memory addresses in another line of code.

For example:
```
[DECLARE:A][QUERYLLM:"List the pros of teaching computer science"]
[DECLARE:B][QUERYLLM:"List the cons of teaching computer science"]
[DECLARE:C][COPYWRITER:"Write a poem that highlights the pros and cons of teaching computer science using the provided lists." USING A + B]
[OUTPUT:C]
```
Unfortunately, the results of the responses using the multi-step process of getting multiple prompts based on the program code were often inferior to just single well defined prompt.

-----
# Important Notes

## Inside scripts:

- main.py -> This is the main loop to execute the functions of the GPT defined program
- memory.py -> This handles the memory object and stores everything GPT has declared to memory
- helper_functions.py -> This handles the parsing of the code lines from the GPT program
- commands.py -> The actual python functions that correspond to the functions in the GPT program
- gpt_functions.py -> This is all purpose function for querying ChatGPT
- logging_functions.py -> Logging for debugging
- search_functions.py, wolfram_functions.py -> Rudimentary searching functions for testing.

## Also noteworthy:

The prompts folders (in data) has the specific roles and prompts for querying GPT depending on certain functions GPT would like to call.

The "documentation" that ChatGPT refers to when deciding how to write the program is in the prompt under generate_program.

# IMPORTANT:

You will need to set up .env with your own API keys in the following format:

```
OPENAI_API_KEY = ""
GOOGLE_API_KEY = ""
GOOGLE_CX = ""
WOLFRAM_APP_ID = ""
```
You will need to install the requirements in requirements.txt
