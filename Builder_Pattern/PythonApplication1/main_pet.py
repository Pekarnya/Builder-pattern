import subprocess
import pet
import os
import pickle
from warnings import WarningMessage
from random import randrange
import test_player as player
import menu as menu

 
class Cat_Director:
    __builder = None
    def set_builder(self, builder):
        self.__builder = builder


    def get_cat (self):
        cat = Cat()

        #Имя

        name = self.__builder.get_name()
        cat.set_name(name)

        #Тело и его состояние

        
        body = self.__builder.get_body()
        cat.set_body(body)

        #Здоровье

        health = self.__builder.get_health()
        cat.set_health(health)

        #Настроение

        mood = self.__builder.get_mood()
        cat.set_mood(mood)

        #Голод

        hungry = self.__builder.get_hungry()
        cat.set_hungry(hungry)

        #Усталость

        tireLvl = self.__builder.get_tireLvl()
        cat.set_tireLvl(tireLvl)

        #Лапки


       # paws = self.__builder.get_paws()
       # cat.attach_paws(paws)

        return cat

    #Персонаж

class Cat:
    def __init__(self):
        #self.__paws = str
        self.__mood = None
        self.__body = None
        self.__health = int
        self.__tireLvl = int
        self.__hungry = int
        self.__name = str

    def set_name (self, name):
        self.__name = name

    def set_body (self, body):
        self.__body = body

    #def attach_paws (self, paws):
       # self.__paws = paws

    def set_health(self, health):
        self.__health = health

    def set_mood (self, mood):
        self.__mood = mood

    def set_hungry (self, hungry):
        self.__hungry = hungry

    def set_tireLvl (self, tireLvl):
        self.__tireLvl = tireLvl

    def HP_status(self):
        HP = self.__health.HP
        return HP

    def save_name(self):
        save_name = self.__name.nick_name
        return save_name

    def hungry_lvl(self):
        hungry_lvl = self.__hungry.hungry_lvl
        return hungry_lvl

    def cat_status (self):

        print ("Имя вашего питомца: % s " % self.__name.nick_name)

        #Здоровье тела производная случайных событий * голод

        print ("Состояние здоровья тела: % s " % self.__body.desiese) #Не забыть описать

        #Голод как производная времени + 10% времени проведенного на улице

        print ("Уровень голода: % s " % self.__hungry.hungry_lvl)

        print ("Количество HP: % d " % self.__health.HP)

        # Настроение как производная ХП и последних событий + 10% усталости + 5% времени проведенного дома без игры +10% уровня голода

        print ("Настроение: % s " % self.__mood.lvl_mood)


        #Усталость производная времени без сна + 10 % времени проведенного на улице

        print ("Уровень усталости: % s " % self.__tireLvl.tirenes)

        # Одежду выбирает пользователь

        #print ("На лапки надеты: % s" % self.__paws.shoes) #Описать обувь (будет смена локаций)
        return self.__name.nick_name


class Cat_builder:



    def get_name (self):
        pass
   # def get_paws (self):
        pass


    def get_body (self):
        pass


    def get_health (self):
        pass


    def get_hungry (self):
        pass

 

    def get_mood (self):
        pass



    def get_tireLvl (self):
        pass

class New_player (Cat_builder):

    def get_name(self):
        name = Name()
        name.nick_name = name.set_nickname()
        return name


   # def get_paws(self):
        paws = Paws()
        print (player.Messages.footwear_message(self))
        paws.shoes = paws.get_paws()
        return paws

    def get_body(self):   
        body = Body()
        body.desiese = body.determ_desiese()
        return body

    def get_health (self):
        health = Health()
        health.HP = Health.HP
        return health

    def get_mood(self):
        mood = Mood()
        mood.lvl_mood = "превосходное настроение "
        return mood

    def get_tireLvl(self):
        tireLvl = TireLvl()
        tireLvl.tirenes = "Бодрствование"
        return tireLvl

    def get_hungry(self):
        hungry = Hungry()
        hungry.hungry_lvl = hungry.hungry_tic()
        return hungry

#Второй строитель для расчета показателей питомца

class Continue_pet(Cat_builder):

    def get_name(self):
        name = Name()
        name.nick_name = name.set_nickname()
        
        return name

   # def get_paws(self):
        paws = Paws()
        print (player.Messages.footwear_message(self))
        paws.shoes = paws.get_paws()
        return paws

    def get_body(self):   
        body = Body()
        body.desiese = body.determ_desiese()
        return body

    def get_health (self):
        health = Health()
        cat = player.LoadSave.load_save()
        HP = cat.HP_status()
        health.HP = Health.set_HP(HP)
        return health


    def get_mood(self):
        mood = Mood()
        mood.lvl_mood = "превосходное настроение "
        return mood

    def get_tireLvl(self):
        tireLvl = TireLvl()
        tireLvl.tirenes = "Бодрствование"
        return tireLvl

    def get_hungry(self):
        hungry = Hungry()
        hungry.hungry_lvl = "Не голоден"
        return hungry






#Классы различных показателей

class Name():

    def set_nickname(self):
        try:
            cat = player.LoadSave.load_save()
            nick_name = cat.save_name()
        except:
            nick_name = None
            nick_name = Name.nick_name = input ("Введите имя вашего питомца ")
        
        return nick_name

class Paws():

    shoes = None

    def get_paws(self):
        shoes = menu.Menu.paws_choose_shoes()
        return shoes




class Health():

    HP = 100

    def set_HP(HP):
        is_feed = menu.Menu.menu_show_feed()
        is_penalty = menu.Menu.is_penalty()
        if is_feed == True:
            HP_tic = 5
        else: 
            HP_tic = -10
        if is_penalty == True:
            penalty_tic = -5
        else:
            penalty_tic = 0

        HP = HP + HP_tic + penalty_tic
        if HP > 100:
            HP = 100
        return HP

class Body():

    desiese = None

    def determ_desiese(self):
        try:
            cat = player.LoadSave.load_save()
            HP = cat.HP_status()

        except: 
            HP = Health.HP

        if HP >= 70:

            desiese = str(player.Desiese_describe.HP_optimum(self))

        if HP < 70:
            #Такой подход позволяет отделить логику игры от содержимого

            desiese = str(player.Desiese_describe.HP_lower_70(self))

        if HP < 30:

            desiese = str(player.Desiese_describe.HP_lower_30(self))

        if HP <= 0:
            desiese = str(player.Messages.end_game(self))
        return desiese

class Mood():

    lvl_mood = None

class TireLvl():

    tirenes = None

class Hungry(Cat):

    hungry_lvl = 10

    def hungry_tic(self):
        hungry_lvl = self.hungry_lvl
        hungry_lvl -= 2
        return hungry_lvl


class Scene:

    def main():
        new_person = New_player() #Инициализируем класс
        cat_director = Cat_Director()
        #Для теста
        cat_director.set_builder(new_person)
        cat = cat_director.get_cat()
        cat.cat_status()
        Scene.render_scene(cat)

    def render_scene(cat):
        player.LoadSave.write_save(cat)
        place_to_go = pet.Walk.place_to_go()
        player.Messages.pet_promenad(place_to_go)
        menu.Menu.shoes_check(place_to_go)
        clear()
        if place_to_go == "Парк":
            pet.Location.Park()
        Scene.continue_scene()


    def continue_scene():   
       continue_screen = Continue_pet()
       director = Cat_Director()
       director.set_builder(continue_screen)
       cat = director.get_cat()
       cat.cat_status()
       Scene.render_scene(cat)

clear = lambda: os.system("cls")
if __name__ == "__main__":
    text = input("Начать новую игру? y/n ")
    if text == "y":
        try:
            os.remove("pet.pickle")
        except:
            print("Это ваша первая игра ")
        Scene.main()
    else:
        Scene.continue_scene()


#Делать что-то дальше без сторонних библиотек нет смысла!
