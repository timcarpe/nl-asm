from memory import *

# Code line class with all the attributes of a code line.
class CodeLine:
    def __init__(self, completed=False, save_to_memory=False, memory_address=None, function=None, description=None, memory_items=None):
        self.completed = completed
        self.save_to_memory = save_to_memory
        self.memory_address = memory_address
        self.function = function
        self.description = description
        self.memory_items = memory_items or []

    def __repr__(self):
        return f"CodeLine(completed={self.completed}, save_to_memory={self.save_to_memory}, memory_address={self.memory_address}, function={self.function}, description={self.description}, memory_items={self.memory_items})"
    
    def __str__(self):
        return f"completed={self.completed}, save_to_memory={self.save_to_memory}, memory_address={self.memory_address}, function={self.function}, description={self.description}, memory_items={self.memory_items}"

# Function to parse a code line into a CodeLine object
def parse_code_line(string):

    # Remove the leading and trailing square brackets
    start = string.find('[')
    end = string.rfind(']')
    string = string[start+1:end]

    # Split the string into command-argument pairs
    if "][" in string:
        pairs = string.split('][')
    # There is only one command-argument pair
    else:
        pairs = [string]

    code_line = CodeLine()

    for pair in pairs:
        if ":" in pair:
            parts = pair.split(':')
            if parts[0] == "DECLARE" and code_line.save_to_memory == False:
                code_line.save_to_memory = True
                code_line.memory_address = parts[1]
            else:
                code_line.function = parts[0]
                # Check if the argument is not a string
                if '"' not in parts[1]:
                    # Check if the argument is a list
                    if " + " in parts[1]:
                        temp = parts[1].split(' + ')
                        for argument in temp:
                            #code_line.memory_items += get_memory_data(str(argument)) + "\n"
                            code_line.memory_items += str(argument)
                    else:
                        code_line.memory_items = str(parts[1])
                #Argument is a string
                elif '"' in parts[1]:
                    #Argument has extra arguments
                    if " USING " in parts[1]:
                        temp = parts[1].split(' USING ')
                        code_line.description = temp[0]
                        # Check if the extra argument is a list
                        if " + " in temp[1]:
                            arguments = temp[1].split(' + ')
                            for argument in arguments:
                                #code_line.memory_items += get_memory_data(str(argument)) + "\n"
                                code_line.memory_items += str(argument)
                        # Checking in case there is no space between the + signs
                        elif "+" in temp[1]:
                            arguments = temp[1].split('+')
                            for argument in arguments:
                                #code_line.memory_items += get_memory_data(str(argument)) + "\n"
                                code_line.memory_items += str(argument)
                        else:
                            #String is just a single argument
                            code_line.memory_items = str(temp[1])
                    else:
                        #String is command/description/task that is wrapped in "" following the :
                        code_line.description = parts[1].replace('"', '')

    return code_line

#This function removes completed code lines from the program. This is useful for future features for GPT driven reflecting and self-improvement while the program is running.
def remove_completed_lines(program):
    for code_line in program:
        if code_line.completed == True:
            program.remove(code_line)
    return program