import sys

def about_error_info(error,error_info : sys):
    file_name = exc_tb.tb_frame.f_code.co_filename
    __,__,exc_tb = error_info.exc_info()
    message = "Error is Occured in python script [{0}] on line number [{1}] message[{3}]".format(
    file_name,exc_tb.tb_lineno.str(error))
    return message

class customexception(Exception):
    def __init__(self,message,error_info: sys):
        super.__init__(message)
        self.message = about_error_info(message,error_info=error_info)
    
    def __str__(self):
        return self.message