#Модули высокого уровня не должны зависеть от модулей низкого уровня.
# Оба типа модулей должны зависеть от абстракций.
#Абстракции не должны зависеть от деталей; детали должны зависеть от абстракций.
#Это позволяет разрабатывать систему более гибкой и способствует её лёгкому тестированию.

#Создадим пример, в котором не используется данный принцип
class Book():
    def read(self):
        print("Чтение интересной истории")

class StoryReader():
    def __init__(self):
        self.book = Book()

    def tell_story(self):
        self.book.read()

#Пример кода с использованием принципа
from abc import ABC, abstractmethod
class StorySource(ABC):
    @abstractmethod
    def get_story(self):
        pass

class Book(StorySource):
    def get_story(self):
        print("Чтение интересной истории")

class AudioBook(StorySource):
    def get_story(self):
        print("Чтение интересной истории вслух")

class StoryReader():
    def __init__(self, story_source: StorySource):
        self.story_sourse = story_source

    def tell_story(self):
        self.story_sourse.get_story()

book = Book()
audioBook = AudioBook()
readerBook = StoryReader(book)
readerAudioBook = StoryReader(audioBook)
readerBook.tell_story()
readerAudioBook.tell_story()