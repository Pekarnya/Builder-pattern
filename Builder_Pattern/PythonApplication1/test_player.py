#Создадим решения игрока
#Director

import webbrowser
from os import name
from abc import ABC, abstractmethod
from random import randrange
import pickle

class Player_director:
    __builder = None
    def set_builder(self, builder):
        self.__builder = builder

    def get_player_moove (self):
        player_moove = Player_moove()
    # Выбор обуви
        paws_choice = self.__builder.get_paws_choice()     
        player_moove.do_paws_choice(paws_choice)    
        #Кормление    
        feed = self.__builder.get_feed_choice()      
        player_moove.do_feed(feed)     
        #Укладывание спать       
        put_tosleep = self.__builder.get_put_tosleep()    
        player_moove.do_put_tosleep(put_tosleep)      
        #Выгул   
        go_walk = self.__builder.get_go_walk()   
        player_moove.do_go_walk (go_walk)       
        #Наказание    
        penalty = self.__builder.get_penalty()    
        player_moove.do_penalty (penalty)

        return player_moove


#То что создаем через билдер

class Player_moove():
    def __init__(self):
        self.__paws_choice = None
        self.__feed = None
        self.__put_tosleep = None
        self.__go_walk = None
        self.__penalty = None
        self.__heal_cat = None

    def do_paws_choice (self, paws_choice):
        self.__paws_choice = paws_choice

    def do_feed (self, feed):
        self.__feed = feed

    def do_put_tosleep (self, put_tosleep):
        self.__put_tosleep = put_tosleep

    def do_go_walk (self, go_walk):
        self.__go_walk = go_walk

    def do_penalty (self, penalty):
        self.__penalty = penalty

    def summary_test (self):
            print (self.__go_walk.state)


# builder
class Player_decide_Builder():
    
    abstractmethod

    def get_paws_choice (self):
        pass
    def get_feed_choice (self):
        pass

    abstractmethod

    def get_put_tosleep (self):
        pass

    abstractmethod

    def get_go_walk (self):
        pass

    abstractmethod

    def get_penalty (self):
        pass


#Основной сборщик информации

class Edit_Player_decide (Player_decide_Builder):

    abstractmethod

    def get_paws_choice(self):
        shoes = Shoes()
        
        shoes.id = input("")
        return shoes


    def get_feed_choice(self):
        food = Food()

        food.item = input("Покормить питомца? y/n ")
        if food.item == "y":
            food.item = True

        return food

    def get_put_tosleep(self):
        dream = Dream()

        dream.state = input("Положить питомца спать? y/n ")
        if dream.state == "y":
            dream.state = True

        return dream

    def get_go_walk(self):
        park = Park()
        park.state = input("Выгулять питомца? y/n")
        if park.state == "y":
            park.state = True

        return park

    def get_penalty(self):
        punch = Punch()
        punch.state == input("Наказать питомца? y/n")
        if punch.state == "y":
            punch.state == True

        return punch

#классы для описания различных ситуаций

class Shoes():
    id = None

class Food():
    item = None

class Dream():
    state = None

class Park():
    state = bool()

class Punch:
    state = None

class Desiese_describe():

    def HP_lower_70(self):
        ache = ["начинается мигрень", "начинается астма", "начинается изжога", "проблемы с печенью"]
        out_ache = str(ache[randrange(0, len(ache))])
        return out_ache

    def HP_lower_30(self):
        ache = ["открылась язва", "начался сепсис", "тахикардия", "нарушена координация", "светобоязнь"]
        out_ache = str(ache[randrange(0, len(ache))])
        return out_ache

    def HP_optimum(self):
        ache = ["ничего не болит", "хоть сейчас в космос", "показатели в норме", "хорошее самочувствие"]
        out_ache = str(ache[randrange(0, len(ache))])
        return out_ache
        

#Переменные для вывода сообщений

class Messages():

    def footwear_message(self):

        message_for_paws = "Выберите обувь для вашего питомца "
        
        return message_for_paws

    def end_game(self):
        print ("Ваш питомец убежал ")
        webbrowser.open_new_tab('https://www.youtube.com/watch?v=TansIl88LW4')
        quit()

    def pet_promenad(place_to_go):
        print("""\n#################Ваш питомец ушел в %s ##########################"""%place_to_go)
        

class LoadSave():

    def write_save(cat):

        with open("pet.pickle", "wb") as f:
                pickle.dump(cat, f)

    def load_save():

        with open('pet.pickle', 'rb') as f:
            cat = pickle.load(f)
        return cat

class Out_data:

    def main():
        new_moovement = Edit_Player_decide() #Инициализируем класс
        player_director = Player_director()

    #Для теста

        player_director.set_builder(new_moovement)
        player = player_director.get_player_moove()
    #   player.summary_test()


if __name__ == "__main__":
    Out_data.main()