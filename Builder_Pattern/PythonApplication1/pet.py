##Поведение питомца
from datetime import datetime
from random import choice

class Walk():

    def place_to_go():
        place = Location.variable_locations()
        pet_place_to_go = choice(place)
        return pet_place_to_go

class Location():

    #Здесь легче в дальнейшем читать локации из файла

    def variable_locations():

        Park = "Парк"
        Library = "Библиотека"
        Home = "Дом"

        place = [Park, Library, Home]

        return place

    def Park():
        return print ("В парке обязательно надо сыграть ")
        
class Season():

    def get_season():
        curent_season = datetime.now()
        month = curent_season.month
        winter = "Зима"
        summer = "Лето"
        autmn = "Осень"
        spring = "Весна"

        if month == 1 or month == 2 or month == 12:
            return winter

        elif month == 6 or month == 7 or month == 8:
            return summer

        elif month == 9 or month == 10 or month == 11:
            return autmn

        elif month == 3 or month == 4 or month == 5:
            return spring