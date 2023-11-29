class address_class:
    def __init__(self, country, city, street, number):
        self.__country = country
        self.__city = city
        self.__street = street 
        self.__number = number

    def get_country(self):
        return self.__country
    
    def get_city(self):
        return self.__city
    
    def get_street(self):
        return self.__street
    
    def get_number_of_the_house(self):
        return self.__number
    
    def __str__(self):
        return self.__country + " | " + self.__city + " | " + self.__street + " | " + self.__number
    