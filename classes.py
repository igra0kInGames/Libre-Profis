import pygame


class Text:
    def __init__(self, screen, text, x, y, fontSize=32, textColor=(0, 0, 0)):
        self.screen = screen
        self.x = x
        self.y = y
        self.fontSize = fontSize
        self.text = text
        self.font = pygame.font.Font(None, fontSize)
        self.textColor = textColor
        self.textSurfaces = self.font.render(self.text, True, self.textColor)

    def draw(self):
        self.screen.blit(self.textSurfaces, (self.x, self.y))

    def setText(self, text):
        self.text = text
        self.textSurfaces = self.font.render(self.text, True, self.textColor)


class Book:
    def __init__(self, id, name, author_name, cover, year):
        if len(id) <= 8:
            if id.find(" "):
                self.id = id
            else:
                print(f"No One space {id}")
                self.id = 0
        else:
            print(f"Too much symbol {id}")
            self.id = 0
        self.name = name
        self.author_name = author_name
        self.cover = cover
        if year.isdigits():
            self.year = year
        else:
            self.year = 1970
            print(f"Year is not number {id}")

    def print_console(self):
        print(f"Книга номер: {self.id}")
        print(f"  Название: {self.name}")
        print(f"  Автор: {self.author_name}")
        print(f"  Обложка: {self.cover}")
        print(f"  Год: {self.year}")
