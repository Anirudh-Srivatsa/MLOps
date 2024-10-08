import sys #This module provides access to some variables used or maintained by the Python interpreter and functions that interact with the interpreter. In this case, sys.exc_info() is used to get details about the exception.
from src.logger import logging

def error_message_detail(error,error_detail:sys): #This function extracts detailed information about where and why an error occurred.
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(file_name,exc_tb.tb_lineno,str(error))

    return error_message

    

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)  # super() is a built-in Python function that gives you access to methods from the parent class (in this case, Exception). It allows you to call methods that are in the parent class without explicitly naming the parent class. This is useful because it keeps your code flexible.
        # super().__init__(error_message) calls the parent class (Exception)’s __init__() method. This ensures that the base functionality of an exception (like storing the error message) is preserved.
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message 
    
if __name__ == "__main__":
    logging.info("Logging has started in the main function.")
    try:
        # Intentional error to trigger logging
        a = 1 / 0
    except Exception as e:
        logging.error("An error occurred", exc_info=True)
        raise CustomException(e, sys) 



'''
    def error_message_detail(error, error_detail: sys): This is a way to define a function in a programming language. The function is called error_message_detail and it takes two inputs or "arguments":
    error: This is some kind of error or problem that has occurred in the program.
    error_detail: sys: This is additional information about the error, and it's specifically getting that information from a module called sys.
    The purpose of this function is to take an error that has happened, along with some extra details about that error, and then do something with that information.
    For example, maybe the function will take the error and the extra details, and then print out a helpful message to the user explaining what went wrong and how they can fix it.

    So in simple terms, this function is a way for a computer program to handle and respond to errors that occur, by using the error information and extra details to provide a useful message to the person using the program.
'''
    
'''
    Tuples are often used to group related pieces of data together, like the three values returned by the exc_info() function in the previous example:
    The exception type
    The exception instance
    The traceback object
    we only care about the traceback that third one(in line 5)
'''

    #python -m src.exception use this id ,src is not recognized