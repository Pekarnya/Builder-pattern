

class Cat_Director:
	__builder = None
	def set_builder(self, builder):
		self.__builder = builder

	def get_cat (self):
		cat = Cat()

		#���� � ��� ���������

		
		body = self.__builder.get_body()
		cat.set_body(body)

		#��������

		health = self.__builder.get_health()
		cat.set_health(health)

		#����������

		mood = self.__builder.get_mood()
		cat.set_mood(mood)

		#�����

		hungry = self.__builder.get_hungry()
		cat.set_hungry(hungry)

		#���������

		tireLvl = self.__builder.get_tireLvl()
		cat.set_tireLvl(tireLvl)

		#�����

		i = 0
		while i < 4:
			paws = self.__builder.get_paws()
			cat.attach_paws(paws)
			i += 1

		return cat

	#��������

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
		#�������� ���� ����������� ��������� ������� * �����

		print ("��������� �������� ����: % s " % self.__body.desiese) #�� ������ �������

		#����� ��� ����������� ������� + 10% ������� ������������ �� �����

		print ("������� ������: % s " % self.__hungry.hungry_lvl)

		print ("���������� HP: % d " % self.__health.HP) #�� ��� ����������� �������� ����

		# ���������� ��� ����������� �� � ��������� ������� + 10% ��������� + 5% ������� ������������ ���� ��� ���� +10% ������ ������

		print ("����������: % s " % self.__mood.lvl_mood)


		#��������� ����������� ������� ��� ��� + 10 % ������� ������������ �� �����

		print ("������� ���������: % s " % self.__tireLvl.tirenes)

		# ������ �������� ������������

		print ("�� ����� ������: %d\'" % self.__paws[0].shoes) #������� ����� (����� ����� �������)

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
		paws.shoes = input ("1) �������� ����� \n 2)������ �����\n 3)������ �����\n ������������ �����")
		try:

			paws.shoes = int(paws.shoes)

		except:

			print ("������� ������ �����")
			paws()

		return paws

	def get_body(self):    #����������!
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

#������ ��������� �����������

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
	new_player = New_player() #�������������� �����
	cat_director = Cat_Director()

	#��� �����

	cat_director.set_builder(new_player)
	cat = cat_director.get_cat()
	cat.cat_status()
	print ("oo8")

if __name__ == "main":
	main()