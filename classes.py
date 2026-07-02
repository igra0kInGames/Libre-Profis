import pygame

class Button:
    def __init__(self, x, y, scaleX, scaleY, bgColor=(255, 255, 255), text="sample text",
                 textColor=(0, 0, 0), fontSize=16, smooth=0, borderSize=-1, screen=None):
        self.x = x
        self.y = y
        self.scaleX = scaleX
        self.scaleY = scaleY
        self.bgColor = bgColor
        self.text = text
        self.textColor = textColor
        self.textSize = fontSize
        self.smooth = smooth
        self.borderSize = borderSize
        self.font = pygame.font.Font(None, fontSize)
        self.screen = screen
        if self.text.count(".") == 0:
            self.textSurfaces = [self.font.render(self.text, True, self.textColor)]
        else:
            self.l = self.text.split('.')
            self.textSurfaces = []
            for i in range(len(self.l)):
                self.textSurfaces.append(self.font.render(self.l[i], True, self.textColor))

    def draw(self):
        pygame.draw.rect(self.screen, self.bgColor, (self.x, self.y, self.scaleX, self.scaleY),
                         border_radius=self.smooth)
        if self.borderSize != -1:
            for i in range(len(self.textSurfaces)):
                self.screen.blit(self.textSurfaces[i], (self.x+5+self.borderSize, self.y+5+self.textSize*i+self.borderSize))
            pygame.draw.rect(self.screen, self.textColor, (self.x, self.y, self.scaleX, self.scaleX), self.borderSize,
                             border_radius=self.smooth)
        else:
            for i in range(len(self.textSurfaces)):
                self.screen.blit(self.textSurfaces[i], (self.x+5, self.y+5+self.textSize*i))

    def isClick(self, event, button=1):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == button \
                    and self.x < x < self.scaleX+self.x \
                    and self.y < y < self.scaleY+self.y:
                return True
            else:
                return False


class Text:
    def __init__(self, screen, text, x, y, fontSize=16, textColor=(0, 0, 0)):
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
