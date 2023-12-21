from MY_CUSTOM_EXCEPTIONS.ui_custom_exception import invalid_option, invalid_option_for_report
def option_exist(option):
    if option not in ["1", "2", "3", "4", "5", "6", "7", "8" , "9", "10", "11", "12", "13", "14"]:
        raise invalid_option("Optiunea aleasa NU exista")
    
def option_for_report_exist(option):
    if option.upper() not in ["A", "B", "C"]:
        raise invalid_option_for_report("Optiunea pentru raport NU exista")
    
def test_option_exist():
    option_exist("1")
    option_exist("2")
    try:
        option_exist("13")
        assert False
    except invalid_option:
        assert True

def test_option_for_report_exist():
    option_for_report_exist("A")
    option_for_report_exist("b")
    option_for_report_exist("C")
    try:
        option_for_report_exist("D")
        assert False
    except invalid_option_for_report:
        assert True