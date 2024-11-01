#пример кода без использования принципа открытости/закрытости

class Report():
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def docPrinter(self):
        print(f"сформирован отчет - {self.title} - {self.content}")
#В итоге у нас получился обычный класс. Теперь представим, что нам нужно его расширить:
# сделать так, чтобы он умел обрабатывать не только обычный текст, но и html.

#Перепишем созданный класс с учётом принципа открытости/закрытости

from abc import ABC, abstractmethod
class Formatted(ABC):
    @abstractmethod
    def format(self, report):
        pass
class TextFormatted(Formatted):
    def format(self, report):
        print(report.title)
        print(report.content)

class HtmlFormatted(Formatted):
    def format(self, report):
        print(f"<h1>{report.title}</h1>")
        print(f"<p>{report.content}</p>")

class Report():
    def __init__(self, title, content, formatted):
        self.title = title
        self.content = content
        self.formatted = formatted

    def docPrinter(self):
        self.formatted.format(self)
report = Report('заголовок отчета', 'это текст отчета, его тут много', TextFormatted())
report.docPrinter()