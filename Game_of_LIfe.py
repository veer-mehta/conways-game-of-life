import pygame, random, time


#SETTINGS
X, Y = 1650, 920
size = 125
theme = "dark"
game_mode = "normal"


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
				pygame.draw.rect(SCREEN, clr_alive, pygame.Rect((scr_by_sz[0])*j, (scr_by_sz[0])*i, scr_by_sz[0], scr_by_sz[0]))
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


def prt(v_nm, x_var, y_var, f_clr, tilt=0, ft = None, bg_clr = None, align = "center"):
    global font
    if ft == None:
        ft = font
    if bg_clr==None:
        text = ft.render(v_nm, True, f_clr)
    else:
        text = ft.render(v_nm, True, f_clr, bg_clr)
    textRect = text.get_rect()
    textRect = (int(x_var), int(y_var))
    if tilt != 0:
        text = pygame.transform.rotate(text, tilt)
    if align == "center":
        textRect = text.get_rect()
        textRect.center = (int(x_var), int(y_var))
    if align == "right":
        text = ft.render(v_nm, True, white)
        textRect = text.get_rect()
        textRect.right = int(x_var)
        textRect[1] = int(y_var)
    SCREEN.blit(text, textRect)


scr_by_sz = X//size, Y//size
l_cells = []
down = False
pygame.init()
SCREEN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

if theme == "dark":
	clr_dead = black()
	clr_alive = white()
else:
	clr_dead = white()
	clr_alive = black()
if game_mode == "creative":
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


f_sz = int(X//51.2)
f_nm = r"..\Fonts\visitor2.ttf"
font = pygame.font.Font(f_nm, f_sz)


prt("Press any key to Start", X//2, Y//2, white(), ft = pygame.font.Font(f_nm, int(100)))
pygame.display.flip()
brk=False
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            brk=True
            break
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    if brk==True:
        break


l_tm = time.time()
while True:	
	if time.time() > l_tm + 0.2:
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
			l_cells[(y//scr_by_sz[0])][(x//scr_by_sz[0])].mode = make
		except:
			pass
