import datetime

log_file = "logs\log.txt"

with (open(log_file, "a")) as f:
    f.write("\n\n--------------------\n\nStarting log at " + str(datetime.datetime.now()) + "\n")

def log_message(message):
    with (open(log_file, "a")) as f:
        f.write(">> " + message + "\n\n")