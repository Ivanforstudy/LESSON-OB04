#Принцип разделения интерфейсов (ISP, Interface Segregation Principle)

#Создадим код без использования данного принципа

class SmartHouse():
    def turn_on_light(self):
        pass

    def heat_food(self):
        pass

    def turn_on_music(self):
        pass

#Согласно принципу разделения интерфейсов нам нужно прописать все эти функции по отдельности,
# как бы сделав для каждого устройства отдельный пульт. Для этого нужно создать каждой функции
# отдельный класс.

class Light():
    def turn_on_light(self):
        print("Свет включен")

class Food():
    def heat_food(self):
        print("Еда начала разогреваться")

class Music():
    def turn_on_music(self):
        print("Включаю подборку ваших любимых песен")