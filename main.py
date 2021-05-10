import pygame, sys
import os
pygame.init()

white = pygame.Color('Gainsboro')

class Music:
    def __init__(self):
        self.W, self.H = 800, 1000
        self.WINDOW = pygame.display.set_mode((self.W, self.H))
        self.WINDOW.fill(white)
        pygame.display.set_caption('Music Player')
        pygame.display.flip()

        self.playing = True

        #Colours
        self.white = (249, 249, 249)
        self.skobeloff = (41, 115, 115)
        self.aquamarine = (133, 255, 199)
        self.coral = (255, 133, 82)
        self.onyx = (69, 68, 76)

        #Text
        self.title_font = pygame.font.Font('media/Phenomena-ExtraLight.otf', 70)
        self.files_font = pygame.font.Font('media/Phenomena-ExtraLight.otf', 25)
        self.music_x = self.W / 5
        self.music_y = self.H / 5

        #Get music files
        self.FileNames = [x.split('.')[0] for x in os.listdir('music/')]

    
    def draw_title(self):
        #Circles
        pygame.draw.circle(self.WINDOW, self.coral, (self.W / 2, -30), 200)
        pygame.draw.circle(self.WINDOW, self.coral, (self.W / 5, self.H / 3), 100)
        pygame.draw.circle(self.WINDOW, self.coral, (self.W / 1.1, self.H / 1.1), 150)

        #Transparent text box
        surface = pygame.Surface((self.W - (self.W / 5 - 50)* 2, self.H), pygame.SRCALPHA)
        surface.fill((249, 249, 249, 180))
        self.WINDOW.blit(surface, (self.W / 5 - 50, self.H / 5 - 22))

        #Title text
        text = self.title_font.render('MUSIC', True, self.onyx)
        title_x = self.W / 2 - text.get_width() / 2
        title_y = self.H / 80
        self.WINDOW.blit(text, (title_x, title_y))

        #Underline
        surface = pygame.Surface((50, 2))
        surface.fill(self.onyx)
        self.WINDOW.blit(surface, (self.W / 2 - 25, title_y + text.get_height() + 2))

    def music_titles(self):
        global text
        if self.FileNames:
            for file in self.FileNames:
                file = file.replace('-', ' ')
                file = file.replace('_', ' ')
                file = file.replace('/', ' ')
                text = self.files_font.render(file, True, self.onyx)
                if self.music_y > self.H / 5.2:
                    rect = text.get_rect()
                    self.WINDOW.blit(text, (self.music_x, self.music_y))
                self.music_y += text.get_height() * 2

            #Resetting text height
            self.music_y -= len(self.FileNames * (text.get_height() * 2))

        else:
            text = self.files_font.render('No files found.', True, self.onyx)
            self.WINDOW.blit(text, (self.W / 2 - text.get_width() / 2, self.H / 3))

    def main(self):
        clock = pygame.time.Clock()
        while self.playing:
            clock.tick(60)
            self.WINDOW.fill(white)
            self.draw_title()
            self.music_titles()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4 and self.music_y < self.H / 5:
                        self.music_y += 30
                    if event.button == 5:
                        self.music_y -= 30


if __name__ == '__main__':
    music = Music()
    music.main()