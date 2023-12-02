from MY_CUSTOM_EXCEPTIONS.validation_exceptions import vid_name_exception, vid_country_exception, vid_city_exception, vid_street_exception, vid_house_number_exception, vid_person_id_exception
class valid_person:
    @staticmethod
    def person_validation(person):
        person_id = person.get_person_id()
        person_name = person.get_person_name()
        person_country = person.get_country()
        person_city = person.get_city()
        person_street = person.get_street()
        person_house_number = person.get_number_of_the_house()
        valid_person.person_id_validation(person_id)
        valid_person.person_name_validation(person_name)
        valid_person.person_country_validation(person_country)
        valid_person.person_city_validation(person_city)
        valid_person.person_street_validation(person_street)
        valid_person.person_house_number_validation(person_house_number)
    
    @staticmethod
    def person_id_validation(person_id):
        if person_id == "":
            raise vid_person_id_exception
    
    @staticmethod
    def person_name_validation(person_name):
        if person_name == "":
            raise vid_name_exception
        
    @staticmethod
    def person_country_validation(person_country):
        if person_country == "":
            raise vid_country_exception
        
    @staticmethod
    def person_city_validation(person_city):
        if person_city == "":
            raise vid_city_exception
    
    @staticmethod
    def person_street_validation(person_street):
        if person_street == "":
            raise vid_street_exception
        
    @staticmethod
    def person_house_number_validation(person_house_number):
        if person_house_number == "":
            raise vid_house_number_exception



