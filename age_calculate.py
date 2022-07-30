from datetime import date
import datetime

today = date.today()
 
def age(birthdate):
    today = date.today()
    age = today.year - birthdate.year- ((today.month, today.day) < (birthdate.month, birthdate.day)) 
    return age

print(age(date(1996,4,13)))




