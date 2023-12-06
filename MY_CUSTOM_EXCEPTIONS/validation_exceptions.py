class event_validation_exception(Exception):
    def __init__(self, validation_error_message):
        self.__validation_error_message = validation_error_message

    def __str__(self):
        return self.__validation_error_message


class vid_event_id_exception(event_validation_exception):
    def __init__(self):
        super().__init__("ERROR : Nu ati introdus un id de event valid. < ID-ul eventului ESTE VID >")

class vid_date_of_event(event_validation_exception):
    def __init__(self):
        super().__init__("ERROR : < Campul datei eventului est vid >")

class vid_duration_of_event(event_validation_exception):
    def __init__(self):
        super().__init__("ERROR : < Campul duratei eventului est vid >")

class vid_description_of_event(event_validation_exception):
    def __init__(self):
        super().__init__("ERROR : < Campul descrierii eventului est vid >")

class invalid_date_character(event_validation_exception):
    def __init__(self, invalid_character_found):
        super().__init__(f"ERROR : Ati introdus un caracter invalid in data. < {invalid_character_found} >")


class invalid_day(event_validation_exception):
    def __init__(self, invalid_day_found):
        super().__init__(f"ERROR : Ati introdus o zi invalida, ziua corespunzatoare datei nu exista in calendar < {invalid_day_found} >")


class invalid_month(event_validation_exception):
    def __init__(self, invalid_month_found):
        super().__init__(f"ERROR : Ati introdus o luna invalida, luna nu exista in calendar < {invalid_month_found} >")


class invalid_year(event_validation_exception):
    def __init__(self, invalid_year_found):
        super().__init__(f"ERROR : Ati introdus un an inexistent, anul introdus trebuie sa fie dupa Hristos < {invalid_year_found} >")


class multiple_dots_in_event_duration(event_validation_exception):
    def __init__(self, invalid_duration_found):
        super().__init__(f"ERROR : Ati introdus mai mult de un punct in durata < {invalid_duration_found} >")


class invalid_event_duration_character(event_validation_exception):
    def __init__(self, invalid_duration_found):
        super().__init__(f"ERROR : Ati introdus o valoare exceptata pentru durata < {invalid_duration_found} >")


class comma_not_supported_in_float_values(event_validation_exception):
    def __init__(self, invalid_duration_found):
        super().__init__(f"ERROR : Ati introdus virgula in durata. daca doriti sa adaugati un numar flotant, separati partea intreaga de partea fractionara prin punct < {invalid_duration_found} >")


class date_incomplete(event_validation_exception):
    def __init__(self, invalid_date_found):
        super().__init__(f"ERROR : Lipseste una din sectiunile: ZI si/sau LUNA si/sau AN  < {invalid_date_found} >")


"""
Exceptii pentru validarea evenimentului:
invalid_date_character, invalid_day, invalid_month, invalid_year, multiple_dots_in_event_duration, invalid_event_duration_character, comma_not_supported_in_float_values, date_incomplete, vid_event_id_exception, vid_date_of_event, vid_duration_of_event, vid_description_of_event

My custom exception for person validation 

"""
class person_validation_exception(Exception):
    def __init__(self, validation_error_message):
        self.__validation_error_message = validation_error_message
    def __str__(self):
        return self.__validation_error_message

class vid_person_id_exception(person_validation_exception):
    def __init__(self):
        super().__init__("ERROR : Nu ati introdus un id de persoana valid. < ID-ul persoanei ESTE VID >")

class vid_name_exception(person_validation_exception):
    def __init__(self):
        super().__init__("ERROR : < CAMPUL NUMELUI ESTE VID >")

class vid_country_exception(person_validation_exception):
    def __init__(self):
        super().__init__("ERROR : < CAMPUL TARII ESTE VID >")

class vid_city_exception(person_validation_exception):
    def __init__(self):
        super().__init__("ERROR : < CAMPUL ORASULUI ESTE VID >")

class vid_street_exception(person_validation_exception):
    def __init__(self):
        super().__init__("ERROR : < CAMPUL STRAZII ESTE VID >")

class vid_house_number_exception(person_validation_exception):
    def __init__(self):
        super().__init__("ERROR : < CAMPUL NUMARULUI CASEI ESTE VID >")



