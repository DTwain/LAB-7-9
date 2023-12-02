from MY_CUSTOM_EXCEPTIONS.ui_custom_exception import invalid_option, invalid_option_for_report
def option_exist(option):
    if option not in ["1", "2", "3", "4", "5", "6", "7", "8" , "9", "10"]:
        raise invalid_option("Optiunea aleasa NU exista")
    
def option_for_report_exist(option):
    if option.upper() not in ["A", "B", "C"]:
        raise invalid_option_for_report("Optiunea pentru raport NU exista")