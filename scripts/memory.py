from logging_functions import log_message

memory_dict = {}

# Create a class to store memory items.
class MemoryItem:
    def __init__(self, address, description, data):
        self.address = address
        self.description = description
        self.data = data

    def __repr__(self):
        return f"Memory(address={self.address}, description={self.description}, data={self.data})"

    def __str__(self):
        return f"address={self.address}, description={self.description}, data={self.data}"

# Add a memory item to the memory dictionary  
def add_memory_item(address, description, data):
    memory_item = MemoryItem(address, description, data)
    # add memory_item to memory_dict with address as key
    memory_dict[address] = memory_item
    log_message("Memory item added: " + str(memory_dict[address]))

# Remove a memory item from the memory dictionary
def remove_memory_item(address):
    # remove memory_item from memory_dict with address as key
    memory_dict.pop(address)

# Get a memory data from the memory dictionary
def get_memory_data(address):
    # return data from memory_item from memory_dict with address as key
    return memory_dict[address].data

# Get a memory description from the memory dictionary
def get_memory_description(address):
    # return description from memory_item from memory_dict with address as key
    return memory_dict[address].description

# Get the full memory state as a string. If fullstate is False only data preview is returned. Useful for previewing memory state when doing GPT driven reflection for reprogramming the code.
def get_memory_state(fullstate = False):

    if fullstate == False:
        memory_state = "Preview Memory State: \naddress, description, data preview\n"
        
        for address, item in memory_dict.items():
            memory_state += item.address + ", "  + item.description + ", " + item.data[0:20] + "...\n\n"
    else:
        memory_state = "Full Memory State: \naddress, description, data\n"
        
        for address, item in memory_dict.items():
            memory_state += str(item) + "\n\n"
    
    return memory_state
