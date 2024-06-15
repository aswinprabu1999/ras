import sys
import logging 


def error_detail_message(error,error_detail:sys):
    _,_,exe_tb=error_detail.exc_info()
    error_message="Error occured in python script name {} line no {} error message is {}" .format(exe_tb.tb_frame.f_code.co_filename,exe_tb.tb_lineno,str(error))
    return error_message                                                                                             
                                                                                                  
                                                                                                
class custom_exception(Exception):
    def __init__(self,error_message,error_detail:sys):
       super().__init__(self,error_message)
       self.error_message=error_detail_message(error_message,error_detail=error_detail)
    def __str__(self):
        return self.error_message
if __name__ == "__main__":
        try:
            a=1/0
        except Exception as e:
            logging.info("ZERO error has occured")
            raise custom_exception (e,sys)

   