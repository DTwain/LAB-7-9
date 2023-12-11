import random
import string

def id_generator() -> str:
    random_id = random.randrange(-100, 100)
    return str(random_id)

def date_generator() -> str:
    random_day = random.randint(-31, 40)  
    random_month = random.randint(-12, 24)
    random_year = random.randint(-100, 2023)  

    date_string = str(random_day) + "/" + str(random_month) + "/" + str(random_year)

    return date_string

def string_generator() -> str:
    size = random.randint(0, 5)
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(size)) 
    # _ este o conventie de nume de variabila care dorim sa fie ignorata

def event_duration_generator() -> str:
    random_duration = random.randint(1, 100)
    return str(random_duration)

def person_number_of_the_house_generator() -> str:
    size = random.randint(0, 5)
    return ''.join(random.choice("123456789ABCDEFG") for _ in range(size))