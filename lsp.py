#Принцип подстановки Барбары Лисков (LSP, Liskov substitution Principle)

#Создадим пример, в котором не используется данный принцип:


class Bird():
    def __init__(self, name):
        self.name = name

    def fly(self):
        print('птица летает')

class Ping(Bird):
    pass
p = Ping ("Сара")
p.fly()

#В нашем случае программа работает не совсем правильно. Мы не можем везде, где будем использовать
# класс Bird, использовать точно так же и класс Ping, так как пингвины не умеют летать и не умеют
# также многого другого, что умеет делать другая птица.

#Создадим код с использованием принципа подстановки Барбары Лисков:

class Bird():
    def fly(self):
        print("эта птица летает")


class Duck(Bird):
    def fly(self):
        print("Эта утка летает быстро")


def fly_in_the_sky(animal):
    animal.fly()

b = Bird()
d = Duck()

fly_in_the_sky(b)
fly_in_the_sky(d)

