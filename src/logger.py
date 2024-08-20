import logging #This module provides a flexible framework for emitting log messages from Python programs. Logs can be recorded at various severity levels such as INFO, WARNING, ERROR, etc.
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # creating a log file with the name in the the given "format.log" and store it as LOG_FILE
logs_path=os.path.join(os.getcwd(),"logs") # this will get you D:\2.0\Project_2.0\MLOps\logs
os.makedirs(logs_path,exist_ok=True) # if logs dic is not there then it creates one

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE) # thhis will join the path with the file name to get eg.D:\2.0\Project_2.0\MLOps\logs\08_16_2024_10_22_30.log

logging.basicConfig( #This sets up the basic configuration for the logging system
    filename=LOG_FILE_PATH, #This sets the log file where the log messages will be written
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO, # This sets the logging level to INFO, meaning only messages at this level or higher (e.g., WARNING, ERROR) will be logged. Lower severity levels like DEBUG won't be logged.


)

if __name__ == "__main__":
    logging.info("Logging has started")

'''
# The strftime() function is a Python function that is used to format a date and time object into a string. It takes a date/time object and a format string as arguments, and returns a string representing the date/time in the specified format.
#os.getcwd(): This gets the current working directory (the directory where your Python script is being executed).
#os.path.join(): This combines the current working directory, the "logs" directory, and the LOG_FILE name into a complete file path for the log file. For example, it could be something like D:\2.0\Project_2.0\MLOps\logs\08_16_2024_10_22_30.log.
#If the "logs" directory doesn't exist in the current working directory, os.path.join() will create it automatically when the path is constructed.

'''

'''
format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s": This defines the format for log messages. Here’s what each placeholder means:
%(asctime)s: Timestamp when the log entry was created.
%(lineno)d: Line number in the source code where the log call was made.
%(name)s: Name of the logger.
%(levelname)s: Severity level of the log (e.g., INFO, ERROR).
%(message)s: The actual log message.'''

'''
The if __name__ == "__main__": block is used to ensure that the code inside it runs only when the script is executed directly and not when it is imported as a module in another script.
In your case, "Logging has started" will be logged when the script is run directly, but it won't be logged if the script is imported elsewhere.
'''