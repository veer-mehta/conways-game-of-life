import pygame, random, time


#INIT PYGAME
X, Y = 750, 750
pygame.init()
SCREEN = pygame.display.set_mode((X, Y))


#COLOURS
global blue, red, green, yellow, cyan, lime, orange, white, black, grey, night_blue

def blue(): return 101, 119, 179
def red(): return 255, 0, 0
def green(): return 72, 161, 77
def yellow(): return 210, 210, 50
def cyan(): return 50, 180, 200
def lime(): return 60, 200, 120
def orange(): return 255, 69, 0
def white(): return 253, 251, 249
def black(): return 0, 0, 0
def grey(): return 150, 150, 150
def night_blue(): return 0, 0, 30


#CLASSES
class Cell:

	def __init__(self, pos, mode):

		self.pos = pos
		self.mode = mode

	def ON(self):
		self.mode = True
	def OFF(self):
		self.mode = False
	def data(self):
		return self.pos, self.mode


def refresh():
	pygame.draw.rect(SCREEN, clr_dead, pygame.Rect(0, 0, X, Y))

	for i in range(size):
		for j in range(size):

			if l_cells[i][j].mode == True:
				pygame.draw.rect(SCREEN, clr_alive, pygame.Rect((scr_by_sz[0])*j, (scr_by_sz[1])*i, scr_by_sz[0], scr_by_sz[1]))
	pygame.display.update()


def update(n_c):
	l_on, l_off = [], []

	for y in range(size):
		for x in range(size):
			nbrs = 0

			for i in range(-1, 2):
				for j in range(-1, 2):
					try:
						if l_cells[y+i][x+j].mode == True and (j, i) != (0, 0):
							nbrs += 1
					except:
						pass

			if (2 <= nbrs <= 3 and n_c[y][x].mode == True) or (nbrs == 3 and n_c[y][x].mode == False):
				l_on.append(n_c[y][x])
			else:
				l_off.append(n_c[y][x])
	for i in l_on:
		i.ON()
	for j in l_off:
		j.OFF()

	return n_c


size = 50
scr_by_sz = X//size, Y//size
l_cells = []
l_true = []

theme = "dark"
if theme == "dark":
	clr_dead = black()
	clr_alive = white()
else:
	clr_dead = white()
	clr_alive = black()
game_mode = "normal"
if game_mode == "create":
	run = False
	for i in range(size):
		a=[]
		for j in range(size):
			a.append(Cell((j, i), False))
		l_cells.append(a)

if game_mode == "normal":
	run = True
	for i in range(size):
		a=[]
		for j in range(size):
			a.append(Cell((j, i), random.choice([True] + [False]*int(size//size**(1/2)))))
		l_cells.append(a)

down = False
l_tm = time.time()
while True:	
	if time.time() > l_tm + 0.25:
		refresh()
		if run == True:
			l_cells = update(l_cells)
		l_tm = time.time()

	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			down = True
			if event.button == 1:
				make = True
			else:make = False

		if event.type == pygame.MOUSEBUTTONUP:
			down = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RETURN:
				run = True
		if event.type == pygame.QUIT:
			exit()
	if down == True:
		x,y = pygame.mouse.get_pos()
		try:
			l_cells[(y//scr_by_sz[1])][(x//scr_by_sz[0])].mode = make
		except:
			pass
