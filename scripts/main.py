from commands import *
from helper_functions import CodeLine
from memory import add_memory_item, get_memory_state, get_memory_data
from logging_functions import log_message


user_goal = input("What would you like to me create? ")

#print("Generating a comparison response...")
#comparison_response = get_gpt_response_content("You are a writer and author. No chat. No user assistance. No verbose. Think step by step.", "Show me a full example: " + user_goal)

program = []

print("Generating program...")

program = generate_program(user_goal)

print("Program generated...")

for code_line in program:

    data = ""
    #print("Running code for: " + str(code_line))

    memory_output = ""

    # Retrieve all data in memory by replacing the address with the data.
    if len(code_line.memory_items) > 0:
        for address in code_line.memory_items:
            memory_output += get_memory_data(address) + "\n\n"
    else:
        #No memory items, so set to none. This is a flag for the functions to know that there is no data to use.
        memory_output = "none"

    # Check the function of the code line and run the appropriate function.
    if code_line.function == "OUTPUT":

        print("Outputting...")

        output_to_user(memory_output)

        code_line.completed = True
        pass

    elif code_line.function == "USERRESPONSE":
        print("Asking for user response...")
        data = userresponse(code_line.description, memory_output)
        # add the response data to the usergoal to maintain context
        user_goal += " " + data
        code_line.completed = True
        pass

    elif code_line.function == "QUERYLLM":
        print("Querying LLM...")
        data = queryllm(user_goal, code_line.description, memory_output)
        code_line.completed = True
        pass

    elif code_line.function == "COPYWRITER":
        print("Requesting copy...")
        data = copywriter(user_goal, code_line.description, memory_output)
        code_line.completed = True
        pass

    elif code_line.function == "SEARCH":
        print("Searching...")
        data = search(code_line.description + " " + memory_output)
        if data == "":
            data = queryllm(user_goal, code_line.description, memory_output)
        code_line.completed = True
        pass

    elif code_line.function == "ANALYZE":
        print("Analyzing...")
        data = analyze(code_line.description + " " + memory_output)
        code_line.completed = True
        pass

    elif code_line.function == "EVALUATE":
        print("Evaluating...")
        data = queryllm(user_goal, code_line.description, memory_output)
        code_line.completed = True
        pass

    else:
        print("Error: Unknown function: " + str(code_line.function))

    if code_line.completed == True and code_line.save_to_memory == True:
        #The code line has been completed and the data should be saved to memory if it is a declare statement
        add_memory_item(code_line.memory_address, code_line.description, data)

#Dump memory to log for debugging
log_message(get_memory_state(True))