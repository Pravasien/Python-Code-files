from abc import ABC, abstractmethod
class Animal(ABC):
	def move(self):
		pass
class Human(Animal):
	def move(self):
		print("I am a human I can walk and run")
class Snake(Animal):
	def move(self):
		print("I am a snake I can crawl")
class Dog(Animal):
	def move(self):
		print("I am a dog I can bark")
class Lion(Animal):
	def move(self):
		print("I am a lion I can roar")
Walk_Run = Human()
Walk_Run.move()
Crawl= Snake()
Crawl.move()
Bark= Dog()
Bark.move()
Roar= Lion()
Roar.move()