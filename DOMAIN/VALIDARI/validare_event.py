import re
from MY_CUSTOM_EXCEPTIONS.validation_exceptions import invalid_date_character, date_incomplete, invalid_month, invalid_year, invalid_day, multiple_dots_in_event_duration, invalid_event_duration_character, comma_not_supported_in_float_values,vid_event_id_exception, vid_date_of_event, vid_duration_of_event, vid_description_of_event

class valid_event:
    def __init__(self) -> None:
        pass

    @staticmethod
    def event_validation(event, choosed_option_ADD_or_UPDATE = "ADD"):
        event_id = event.get_event_id()
        event_date = event.get_event_date()
        event_duration = event.get_event_duration()
        event_description = event.get_event_description()
        valid_event.event_id_validation(event_id)
        valid_event.event_date_validation(event_date, choosed_option_ADD_or_UPDATE)
        valid_event.event_duration_validation(event_duration, choosed_option_ADD_or_UPDATE)
        valid_event.event_description_validation(event_description, choosed_option_ADD_or_UPDATE)
    
    @staticmethod
    def event_validation_for_update(event, choosed_option_ADD_or_UPDATE = "UPDATE"):
        event_id = event.get_event_id()
        event_date = event.get_event_date()
        event_duration = event.get_event_duration()
        event_description = event.get_event_description()
        valid_event.event_id_validation(event_id)
        valid_event.event_date_validation(event_date, choosed_option_ADD_or_UPDATE)
        valid_event.event_duration_validation(event_duration, choosed_option_ADD_or_UPDATE)
        valid_event.event_description_validation(event_description, choosed_option_ADD_or_UPDATE)

    @staticmethod
    def event_id_validation(event_id):
        if event_id == "":
            raise vid_event_id_exception
 
    @staticmethod
    def event_date_sintax_evaluation(event_date, choosed_option_ADD_or_UPDATE):
        for character in event_date:
            if character not in "/.:0123456789":
                raise invalid_date_character(character)
        if choosed_option_ADD_or_UPDATE == "ADD":
            if event_date == "":
                raise vid_date_of_event

    @staticmethod
    def event_date_logic_evaluation(event_date):
        zi_luna_an = re.split(r'[:./]', event_date) 
        zi_luna_an = [int(x) for x in zi_luna_an if x != '']

        if len(zi_luna_an) != 3:
            raise date_incomplete(zi_luna_an) # daca nu am 3 elemente in lista inseamna ca nu am introdus data corect
        
        zi = zi_luna_an[0]
        luna = zi_luna_an[1]
        an = zi_luna_an[2]

        if luna <= 0 or luna > 12:
            raise invalid_month(luna)
        if an <= 0:
            raise invalid_year(an)
        if zi <= 0 or zi > 31:
            raise invalid_day(zi)
        
        #verific daca anul este bisect
        bisect = False
        if an % 4 == 0:
            bisect = True
        else:
            bisect = False
        if an % 100 == 0:
            bisect = False
        if an % 400 == 0:
            bisect = True
        if luna == 1 or luna == 3 or luna == 5 or luna == 7 or luna == 8 or luna == 10 or luna == 12:
            if zi > 31:
                raise invalid_day(zi)
        if luna == 4 or luna == 6 or luna == 9 or luna == 11:
            if zi > 30:
                raise invalid_day(zi)
        if luna == 2 and bisect == False:
            if zi > 28:
                raise invalid_day(zi)
        if luna == 2 and bisect == True:
            if zi > 29:
                raise invalid_day(zi)

    @staticmethod
    def event_date_validation(event_date, choosed_option_ADD_or_UPDATE):
        valid_event.event_date_sintax_evaluation(event_date, choosed_option_ADD_or_UPDATE)
        if event_date != "":
            valid_event.event_date_logic_evaluation(event_date)

    @staticmethod
    def event_duration_validation(event_duration, choosed_option_ADD_or_UPDATE):
        dot_counter = 0 
        for character in event_duration:
            if character == '.':
                dot_counter += 1
            if dot_counter >= 2:
                raise multiple_dots_in_event_duration(event_duration)
            if character == ',':
                raise comma_not_supported_in_float_values(event_duration)
            if  character not in ".0123456789":
                raise invalid_event_duration_character(event_duration)
        if choosed_option_ADD_or_UPDATE == "ADD":
            if event_duration == "":
                raise vid_duration_of_event
    
    @staticmethod
    def event_description_validation(event_description, choosed_option_ADD_or_UPDATE):
        if choosed_option_ADD_or_UPDATE == "ADD":
            if event_description == "":
                raise vid_description_of_event
        
       

            
        

        

