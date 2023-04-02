

class Cat_Director:
	__builder = None
	def set_builder(self, builder):
		self.__builder = builder

	def get_cat (self):
		cat = Cat()

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

		i = 0
		while i < 4:
			paws = self.__builder.get_paws()
			cat.attach_paws(paws)
			i += 1

		return cat

	#Персонаж

class Cat:
	def __init__(self):
		self.__paws = list()
		self.__mood = None
		self.__body = None
		self.__health = int
		self.__tireLvl = int
		self.__hungry = int

	def set_body (self, body):
		self.__body = body

	def attach_paws (self, paws):
		self.__paws.append(paws)

	def set_health(self, health):
		self.__health = health

	def set_mood (self, mood):
		self.__mood = mood

	def set_hungry (self, hungry):
		self.__hungry = hungry

	def set_tireLvl (self, tireLvl):
		self.__tireLvl = tireLvl

	def cat_status (self):
		#Здоровье тела производная случайных событий * голод

		print ("Состояние здоровья тела: % s " % self.__body.desiese) #Не забыть описать

		#Голод как производная времени + 10% времени проведенного на улице

		print ("Уровень голода: % s " % self.__hungry.hungry_lvl)

		print ("Количество HP: % d " % self.__health.HP) #Хп как производная здоровья тела

		# Настроение как производная ХП и последних событий + 10% усталости + 5% времени проведенного дома без игры +10% уровня голода

		print ("Настроение: % s " % self.__mood.lvl_mood)


		#Усталость производная времени без сна + 10 % времени проведенного на улице

		print ("Уровень усталости: % s " % self.__tireLvl.tirenes)

		# Одежду выбирает пользователь

		print ("На лапки надеты: %d\'" % self.__paws[0].shoes) #Описать обувь (будет смена локаций)

class cat_builder:
	def get_paws (self):
		pass
	def get_body (self):
		pass
	def get_helth (self):
		pass
	def get_hungry (self):
		pass
	def get_mood (self):
		pass
	def get_tireLvl (self):
		pass

class New_player (cat_builder):

	def get_paws(self):
		paws = Paws()
		paws.shoes = input ("1) домашняя обувь \n 2)зимняя обувь\n 3)летняя обувь\n демисезонная обувь")
		try:

			paws.shoes = int(paws.shoes)

		except:

			print ("Вводите только числа")
			paws()

		return paws

	def get_body(self):    #Доработать!
		body = Body()
		shoes_impact = ""
		stomach = ""
		head = ""
		desiese = shoes_impact + stomach + head

		return desiese

	def get_helth (self):
		health = Health()
		return health

	def get_mood(self):
		mood = Mood()
		return mood

	def get_tireLvl(self):
		tireLvl = TireLvl()
		return tireLvl

	def get_hungry(self):
		hungry = Hungry()
		return hungry

#Классы различных показателей

class Paws():

	shoes = None

class Body():

	desiese = None

class Health():

	HP = None

class Mood():

	lvl_mood = None

class TireLvl():

	tirenes = None

class Hungry():

	hungry_lvl = None
	
def main():
	new_player = New_player() #Инициализируем класс
	cat_director = Cat_Director()

	#Для теста

	cat_director.set_builder(new_player)
	cat = cat_director.get_cat()
	cat.cat_status()
	print ("oo8")

if __name__ == "main":
	main()