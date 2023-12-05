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
    
    def set_country(self, new_country):
        self.__country = new_country

    def set_city(self, new_city):
        self.__city = new_city
    
    def set_street(self, new_street):
        self.__street = new_street
    
    def set_number_of_the_house(self, new_number):
        self.__number = new_number
        
    
    def __str__(self):
        return "Tara:      " + self.__country + "\nOras:      " + self.__city + "\nStrada:    " + self.__street + "\nNumar:     " + self.__number
    