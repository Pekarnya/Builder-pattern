#Меню и интерфейс
import main_pet as pet
import test_player as player
import pet as logic

class Menu():

    def user_input(x):
        user_input_feed = input(x)
        if user_input_feed == "y":
            return True
        else:
            return False

    def menu_show_feed():
        feed = "{:#^44} ".format(" Покормить питомца? y/n ")
        user_input = Menu.user_input(feed)
        return user_input

    def is_penalty():
        penalty = "{:#^44} ".format(" Наказать питомца? y/n ")
        user_input = Menu.user_input(penalty)
        return user_input

    def paws_choose_shoes():
        home_shoes = "домашняя обувь"
        winter_shoes = "зимняя обувь"
        summer_shoes = "летняя обувь"
        autmn_shoes = "демисезонная обувь"
        shoes_choice = input ("1)" + home_shoes + "\n 2)" + winter_shoes + "\n 3)" + summer_shoes + "\n 4" + autmn_shoes + " " )
        try:

            if shoes_choice == "1":
               shoes = home_shoes
                

            elif shoes_choice == "2":
                shoes = winter_shoes

            elif shoes_choice == "3":
                shoes = summer_shoes

            elif shoes_choice == "4":
                shoes = autmn_shoes

        except:
            print ("Вводите только числа указанные в меню")
        return shoes

    def shoes_check(place_to_go):
        season = logic.Season.get_season()
        shoes_for_walk = "{:#^44} ".format(" Выберите подходящую обувь для %s " %place_to_go)
        print (shoes_for_walk)
        print ("\n Сейчас %s " %season)
        shoes = Menu.paws_choose_shoes()





