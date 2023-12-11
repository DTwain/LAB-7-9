import random
import string

def id_generator():
    random_id = random.randrange(-100, 100)
    return random_id

def date_generator():
    random_day = random.randint(-31, 40)  
    random_month = random.randint(-12, 24)
    random_year = random.randint(-100, 2023)  

    date_string = str(random_day) + "/" + str(random_month) + "/" + str(random_year)

    return date_string

def string_generator(size):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(size)) 
    # _ este o conventie de nume de variabila care dorim sa fie ignorata

def event_duration_generator():
    random_duration = random.randint(1, 100)
    return str(random_duration)