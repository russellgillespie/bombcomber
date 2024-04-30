#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from random import randrange
from time import sleep, time


class MyGame(object):

    def __init__(
        self,
        width,
        height,
        boardsize=1,
        minedensity=2,
        ):

        # initialize variables for user-defined difficulty and mine density

        self.boardsize = boardsize
        self.minedensity = minedensity

        (self.width, self.height) = (width, height)
        self.hud_height = 100
        self.tile_size = 50 * self.boardsize
        self.tilew = int(self.width / self.tile_size)
        self.tileh = int((self.height - self.hud_height)
                         / self.tile_size)

        self.screen = pygame.display.set_mode((self.width, self.height))

        self.clock = pygame.time.Clock()
        self.start_time = time()

        self.score = 0
        self.minescore = 0
        self.mines_left = 0
        self.lose = False
        self.win = False

        self.initFonts()
        self.initGraphics()
        self.initSounds()
        self.initNumMines()
        self.adjMatrix = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.initMatrix()
        self.initBG()
        self.initMines()
        self.initNum()
        self.initMap()
        self.initVoidCheck()

        bg_Music.play(loops=-1)

    def initFonts(self):

    # create font

        self.myfont = pygame.font.SysFont(None, 32)
        self.myfont64 = pygame.font.Font('Chalkduster.ttf', 64)
        self.myfont96 = pygame.font.Font('Chalkduster.ttf', 96)
        self.fixed48 = pygame.font.Font('SimSun-ExtB.ttf', 48)
        self.myfont20 = pygame.font.SysFont(None, 20)

    def initMatrix(self):
        self.matrix = []
        for x in range(-1, 2):
            for y in range(-1, 2):
                if (x, y) != (0, 0):
                    self.matrix.append((x, y))

    def initGraphics(self):
        self.tile = pygame.image.load('tile.png')
        self.tiledown = pygame.image.load('tiledown.png')

# ........self.background=pygame.image.load("background.png")

        self.hudBG = pygame.image.load('hudBG.png')
        self.mine = pygame.image.load('mine.png')
        self.flag = pygame.image.load('comb.png')
        self.num1 = pygame.image.load('num1.png')
        self.num2 = pygame.image.load('num2.png')
        self.num3 = pygame.image.load('num3.png')
        self.num4 = pygame.image.load('num4.png')
        self.num5 = pygame.image.load('num5.png')
        self.num6 = pygame.image.load('num6.png')
        self.num7 = pygame.image.load('num7.png')
        self.num8 = pygame.image.load('num8.png')
        self.num9 = pygame.image.load('num9.png')
        self.num0 = pygame.image.load('num0.png')
        self.gameover = pygame.image.load('gameover.png')
        self.winscreen = pygame.image.load('winscreen.png')
        self.win_blank = pygame.image.load('win_blank.png')

        # scale all images based on difficulty

        self.tile = pygame.transform.scale(self.tile,
                (int(self.tile_size), int(self.tile_size)))
        self.tiledown = pygame.transform.scale(self.tiledown,
                (int(self.tile_size), int(self.tile_size)))

# ........self.background=pygame.transform.scale(self.background, (int(self.tile_size), int(self.tile_size)))

        self.mine = pygame.transform.scale(self.mine,
                (int(self.tile_size), int(self.tile_size)))
        self.flag = pygame.transform.scale(self.flag,
                (int(self.tile_size), int(self.tile_size)))
        self.num1 = pygame.transform.scale(self.num1,
                (int(self.tile_size), int(self.tile_size)))
        self.num2 = pygame.transform.scale(self.num2,
                (int(self.tile_size), int(self.tile_size)))
        self.num3 = pygame.transform.scale(self.num3,
                (int(self.tile_size), int(self.tile_size)))
        self.num4 = pygame.transform.scale(self.num4,
                (int(self.tile_size), int(self.tile_size)))
        self.num5 = pygame.transform.scale(self.num5,
                (int(self.tile_size), int(self.tile_size)))
        self.num6 = pygame.transform.scale(self.num6,
                (int(self.tile_size), int(self.tile_size)))
        self.num7 = pygame.transform.scale(self.num7,
                (int(self.tile_size), int(self.tile_size)))
        self.num8 = pygame.transform.scale(self.num8,
                (int(self.tile_size), int(self.tile_size)))
        self.num9 = pygame.transform.scale(self.num9,
                (int(self.tile_size), int(self.tile_size)))
        self.num0 = pygame.transform.scale(self.num0,
                (int(self.tile_size), int(self.tile_size)))

    def initSounds(self):
        pass

    def initNumMines(self):
        self.numMines = {}
        self.numMines[0] = self.num0
        self.numMines[1] = self.num1
        self.numMines[2] = self.num2
        self.numMines[3] = self.num3
        self.numMines[4] = self.num4
        self.numMines[5] = self.num5
        self.numMines[6] = self.num6
        self.numMines[7] = self.num7
        self.numMines[8] = self.num8
        self.numMines[9] = self.num9

    def initBG(self):
        self.bg = {}
        self.bg = [[False for y in range(self.tileh)] for x in
                   range(self.tilew)]

# ........for x in range(self.tilew):
# ............for y in range(self.tileh):
# ................self.bg[x][y] = self.background

    def initMines(self):
        self.mines = {}
        self.mines = [[False for y in range(self.tileh)] for x in
                      range(self.tilew)]

        for x in range(self.tilew):
            for y in range(self.tileh):
                draw_mine = randrange(10)
                if draw_mine < self.minedensity:
                    self.mines[x][y] = self.mine
                    self.minescore += 1

    def initNum(self):
        for x in range(self.tilew):
            for y in range(self.tileh):
                self.bg[x][y] = self.countMines(x, y)

    def initVoidCheck(self):
        self.voidCheck = {}
        self.voidCheck = [[False for y in range(self.tileh)] for x in
                          range(self.tilew)]

    def initMap(self):

        # initialize tilemap dictionary

        self.map = {}
        self.map = [[False for y in range(self.tileh)] for x in
                    range(self.tilew)]

        for x in range(self.tilew):
            for y in range(self.tileh):
                self.map[x][y] = self.tile

    def drawBG(self):
        for x in range(self.tilew):
            for y in range(self.tileh):
                self.screen.blit(self.numMines[self.bg[x][y]], (x
                                 * self.tile_size, y * self.tile_size))

    def drawHUD(self):
        self.screen.blit(self.hudBG, (0, self.height - self.hud_height))
        hud_offset = self.height - self.hud_height / 2

        # Determine time elapsed

        elapsed = time() - self.start_time
        (m, s) = divmod(elapsed, 60)

        # create text surface

        time_display = self.fixed48.render('%02d:%02d' % (m, s), 1,
                (50, 50, 50))
        score = self.myfont64.render('Score:%02d' % self.score, 1,
                (244, 249, 253))
        mines_left = self.myfont64.render('Bombs:%d' % self.mines_left,
                1, (244, 249, 253))

        # draw surface

        time_align = self.width / 2 - time_display.get_width() / 2
        self.screen.blit(time_display, (time_align, hud_offset
                         - time_display.get_height() // 2))
        self.screen.blit(score, (20, hud_offset - score.get_height()
                         // 2))
        self.screen.blit(mines_left, (self.width
                         - mines_left.get_width() - 20, hud_offset
                         - mines_left.get_height() // 2))

    def drawMines(self):
        for x in range(self.tilew):
            for y in range(self.tileh):
                if self.mines[x][y] != False:
                    self.screen.blit(self.mines[x][y], (x
                            * self.tile_size, y * self.tile_size))

    def drawMap(self):
        for x in range(self.tilew):
            for y in range(self.tileh):
                try:
                    if self.map[x][y] != False:
                        self.screen.blit(self.map[x][y], (x
                                * self.tile_size, y * self.tile_size))
                except:
                    self.screen.blit(self.flag, (x * self.tile_size, y
                            * self.tile_size))

    def countMines(self, xpos, ypos):
        self.count = 0

        # Check all adjacent and diagonal tiles for mines and add to count

        for (x, y) in self.matrix:
            try:
                if self.mines[xpos + x][ypos + y] != False and xpos \
                    < self.tilew and xpos + x >= 0 and ypos \
                    < self.tileh and ypos + y >= 0:
                    self.count += 1
            except:
                pass
        return self.count

    def fillVoid(self, xpos, ypos):

        # Check all adjacent squares for voids....

        for (x, y) in self.matrix:
            try:
                if xpos + x >= 0 and ypos + y >= 0:
                    self.map[xpos + x][ypos + y] = False
                if self.bg[xpos + x][ypos + y] == 0 \
                    and self.voidCheck[xpos + x][ypos + y] == False \
                    and xpos + x >= 0 and ypos + y >= 0:
                    self.voidCheck[xpos + x][ypos + y] = True
                    self.fillVoid(xpos + x, ypos + y)
                else:
                    pass
            except:
                pass

# ........for time in range(2):

        self.voidConnect()

    def voidConnect(self):
        for row in range(self.tilew):
            for col in range(self.tileh):
                for (x, y) in self.matrix:
                    try:
                        if self.voidCheck[row + x][col + y] == True \
                            and row + x >= 0 and col + y >= 0:
                            self.map[row][col] = False
                        else:
                            pass
                    except:
                        pass

    def countScore(self):
        self.score = 0
        self.mines_left = 0
        for x in range(self.tilew):
            for y in range(self.tileh):
                if self.map[x][y] == 'flag':
                    self.score += 1
        self.mines_left = self.minescore - self.score

    def gamewin(self):
        if self.minescore == self.score:
            map_clear = 0
            for x in range(self.tilew):
                for y in range(self.tileh):
                    if self.map[x][y] == False:
                        map_clear += 1
            if map_clear + self.score == self.tilew * self.tileh:
                sfx_win.play()
                self.win = True
                for x in range(self.tilew):
                    for y in range(self.tileh):
                        self.map[x][y] = False
                        self.drawMines()
                self.screen.blit(self.win_blank, (0, 0))
                iwin = self.myfont96.render("You're the Bomb!", 1, (0,
                        0, 0))
                self.screen.blit(iwin, (self.width / 2
                                 - iwin.get_width() / 2, self.height
                                 / 2 - iwin.get_height() / 2))
                pygame.display.flip()

    def update(self):
        self.gamewin()
        if self.lose == True:
            bg_Music.stop()
            click_to_continue()
        elif self.win == True:
            bg_Music.stop()
            click_to_continue()
        else:
            pass

        self.clock.tick(24)
        self.screen.fill(0)

        self.drawBG()
        self.drawMines()
        self.drawMap()
        self.drawHUD()

        mouse_pressed = pygame.mouse.get_pressed()
        (xpos, ypos) = pygame.mouse.get_pos()
        xpos = xpos // int(self.tile_size)
        ypos = ypos // int(self.tile_size)

        # Event Handling

        event = pygame.event.poll()

        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN \
            and self.map[xpos][ypos] != False:
            match.play()
        if mouse_pressed[0] == True and self.map[xpos][ypos] != False:
            self.screen.blit(self.tiledown, (xpos * self.tile_size,
                             ypos * self.tile_size))
        try:
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if self.mines[xpos][ypos] == False:
                    self.map[xpos][ypos] = False
                    if self.bg[xpos][ypos] == 0:
                        self.fillVoid(xpos, ypos)
                else:
                    self.map[xpos][ypos] = False
                    for x in range(self.tilew):
                        for y in range(self.tileh):
                            self.map[x][y] = False
                            self.drawMines()
                    explode.play()
                    self.screen.blit(self.gameover, (0, 0))
                    self.lose = True
            elif event.type == pygame.MOUSEBUTTONUP and event.button \
                == 3:

                if self.map[xpos][ypos] == 'flag':
                    self.map[xpos][ypos] = self.tile
                elif self.map[xpos][ypos] != False:
                    self.map[xpos][ypos] = 'flag'
                else:
                    pass
            else:
                pass
        except:
            pass

        self.countScore()

        pygame.event.pump()

        pygame.display.flip()


def menu():
    menu_surface = pygame.Surface((width, height))
    menu_surface.blit(splash, (0, 0))
    splash_loop.play(-1)

    myfont = pygame.font.Font('Chalkduster.ttf', 48)

    while 1:
        selected = [(244, 249, 253), (244, 249, 253), (244, 249, 253),
                    (244, 249, 253)]
        difficulty = [(1, 1), (1, 2), (.5, 1), (.5, 2)]

        (x, y) = pygame.mouse.get_pos()
        selector = y // (height / 8) - 3
        if selector < 0:
            selector = 0
        if selector > 3:
            selector = 3

        try:
            selected[int(selector)] = (238, 143, 41)
        except IndexError:
            pass

        try:
            if to_click != selected:
                menu_click.play()
        except:
            pass

        to_click = selected

        easy = myfont.render('easy', 1, selected[0])
        normal = myfont.render('normal', 1, selected[1])
        hard = myfont.render('hard', 1, selected[2])
        expert = myfont.render('expert', 1, selected[3])

        menu_surface.blit(easy, (width // 2 - easy.get_width() // 2,
                          height * 3 // 8))
        menu_surface.blit(normal, (width // 2 - normal.get_width()
                          // 2, height * 4 // 8))
        menu_surface.blit(hard, (width // 2 - hard.get_width() // 2,
                          height * 5 // 8))
        menu_surface.blit(expert, (width // 2 - expert.get_width()
                          // 2, height * 6 // 8))

        screen.blit(menu_surface, (0, 0))

        event = pygame.event.poll()
        if event.type == pygame.MOUSEBUTTONUP:
            try:
                splash_loop.stop()
                fuse.play()
                (boardsize, minedensity) = difficulty[int(selector)]
                new_game(width, height, boardsize, minedensity)
            except IndexError:
                pass
        elif event.type == pygame.QUIT:
            exit()

        pygame.display.flip()
        pygame.event.pump()


def click_to_continue():
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                menu()
            elif event.type == pygame.QUIT:
                exit()
        pygame.display.flip()


# Create Main Game Class Object

def new_game(
    width,
    height,
    boardsize,
    minedensity,
    ):
    game = MyGame(width, height, boardsize, minedensity)

    # Main Game Loop

    while 1:
        game.update()


# Configure Pygame Window........

pygame.init()
(width, height) = (1000, 700)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Bomb Comber')

# Load Splash Image

splash = pygame.image.load('splash.png')

# Load Audio Files

splash_loop = pygame.mixer.Sound(file='splash.aif')
menu_click = pygame.mixer.Sound(file='menu_click.aif')
explode = pygame.mixer.Sound(file='explode.aif')
match = pygame.mixer.Sound(file='match.aif')
match.set_volume(.1)
bg_Music = pygame.mixer.Sound(file='bombcomber.aif')
bg_Music.set_volume(.5)
fuse = pygame.mixer.Sound(file='fuse.aif')
fuse.set_volume(.5)
sfx_win = pygame.mixer.Sound(file='win.aif')

menu()

# ....new_game(width, height, boardsize, minedensity)
