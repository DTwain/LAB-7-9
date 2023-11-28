class event_validation_exception(Exception):
    def __init__(self, validation_error_message):
        self.__validation_error_message = validation_error_message

    def __str__(self):
        return self.__validation_error_message


class vid_id_exception(event_validation_exception):
    def __init__(self):
        super().__init__("ERROR : Nu ati introdus un id valid. <ID_UL ESTE VID>\n")


class invalid_date_character(event_validation_exception):
    def __init__(self, invalid_character_found):
        super().__init__(f"ERROR : ATI INTRODUS UN CARACTER INVALID. < {invalid_character_found} >\n")


class invalid_day(event_validation_exception):
    def __init__(self, invalid_day_found):
        super().__init__(f"ERROR : Ati introdus o zi invalida, ziua nu exista in calendar < {invalid_day_found} >\n")


class invalid_month(event_validation_exception):
    def __init__(self, invalid_month_found):
        super().__init__(f"ERROR : Ati introdus o luna invalida, luna nu exista in calendar < {invalid_month_found} >\n")


class invalid_year(event_validation_exception):
    def __init__(self, invalid_year_found):
        super().__init__(f"ERROR : Ati introdus un an inexistent, anul introdus trebuie sa fie dupa hristos < {invalid_year_found} >\n")


class multiple_dots_in_event_duration(event_validation_exception):
    def __init__(self, invalid_duration_found):
        super().__init__(f"ERROR : Ati introdus mai mult de un punct in durata < {invalid_duration_found} >\n")


class invalid_event_duration_character(event_validation_exception):
    def __init__(self, invalid_duration_found):
        super().__init__(f"ERROR : Ati introdus o valoare exceptata pentru durata < {invalid_duration_found} >\n")


class comma_not_supported_in_float_values(event_validation_exception):
    def __init__(self, invalid_duration_found):
        super().__init__(f"ERROR : Ati introdus virgula in durata. daca doriti sa adaugati un numar flotant, separati partea intreaga de partea fractionara prin punct < {invalid_duration_found} >\n")


class date_incomplete(event_validation_exception):
    def __init__(self, invalid_date_found):
        super().__init__(f"ERROR : Lipseste una din sectiunile: ZI si/sau LUNA si/sau AN  < {invalid_date_found} >\n")


"""
My custom exception for person validation 

"""
class person_validation_exception(Exception):
    def __init__(self, validation_error_message):
        self.__validation_error_message = validation_error_message
    def __str__(self):
        return self.__validation_error_message

class vid_name_exception(person_validation_exception):
    def __init__(self):
        super().__init__("ERROR : < CAMPUL NUMELUI ESTE VID >\n")

class vid_country_exception(person_validation_exception):
    def __init__(self):
        super().__init__("ERROR : < CAMPUL TARII ESTE VID >\n")

class vid_city_exception(person_validation_exception):
    def __init__(self):
        super().__init__("ERROR : < CAMPUL ORASULUI ESTE VID >\n")

class vid_street_exception(person_validation_exception):
    def __init__(self):
        super().__init__("ERROR : < CAMPUL STRAZII ESTE VID >\n")

class vid_house_number_exception(person_validation_exception):
    def __init__(self):
        super().__init__("ERROR : < CAMPUL NUMARULUI CASEI ESTE VID >\n")


