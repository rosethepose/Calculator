import pygame
import sys
import os
import random
from pygame.locals import *


def init(data):
     data.top = 75
     data.keys = [["7", "8", "9", "+"],["4","5","6","-"],["1","2","3","*"],["<-","0","=","/"]]
     data.code = ""

# event.key returns an int value for the key in ASCII
def keyDown(event, data):
    pass

# event.key returns an int value for the key in ASCII
def keyUp(event, data):
    pass

# event.pos = x,y to get coordinates of mouse pressed
def mouseDown(event, data):
    mouseX, mouseY = event.pos
    #if mouseY > data.top:

    mouseY -= data.top
    rowClicked = 5*mouseY // data.height
    colClicked = 4*mouseX // data.width
    print(rowClicked, colClicked)
    if rowClicked == 3 and colClicked == 0: #backspace
          data.code = data.code[:-2]
    elif rowClicked == 3 and colClicked== 2: #equals sign
          data.code = runCode(data)
    else: # number / symbol key pressed
           data.code += data.keys[rowClicked][colClicked] + " "

def runCode(data):
	eq = data.code.rstrip()
	myList = eq.split(' ')
	count = len(myList)
	a = 0
	for x in range(a, count):
		if myList[0].isnumeric():
			num = int(myList[0])
			myList.append(num)
			myList.pop(0)
			a = 0
		elif myList[0] == '+':
			myList.append(myList.pop() + myList.pop())
			myList.pop(0)
		elif myList[0] == '-':
			first = myList.pop()
			second = myList.pop()
			myList.append(second - first)
			myList.pop(0)
		elif myList[0] == '*':
			myList.append(myList.pop() * myList.pop())
			myList.pop(0)
		elif myList[0] == '/':
			first = myList.pop()
			second = myList.pop()
			myList.append(second / first)
			myList.pop(0)
		else:
			print("Error!")
	return(str(myList[0]))
	data.code = myList[0]

# event.pos = x,y to get coordinates of mouse pressed
def mouseUp(event, data):
    pass

# controlled by the refresh rate in data.clock
def timerFired(data):
    pass

def redrawAll(screen, data):
     pygame.draw.rect(screen, (225,225,225), (0,0, data.width, data.top))
     drawText(data.code, font, screen, 15, data.top - 55, (0,0,0))
     rowHeight = (data.height - data.top) // 4
     colWidth = data.width // 4
     #pygame.draw.rect(screen, (128,128,128), (0,0, data.width, data.top))

     for row in range(4): #adds rows
          for col in range(4): #adds columns
               pygame.draw.rect(screen, (225,225,225), (col*colWidth, row*rowHeight + data.top, colWidth, rowHeight))
               pygame.draw.rect(screen, (100,100,255), (col*colWidth + 5, row*rowHeight + data.top + 5, colWidth - 10, rowHeight - 10))
               drawText(data.keys[row][col], font, screen, col*colWidth + 50, row*rowHeight + data.top + 40)

# draw text function. Do not change.
def drawText(displayString, font, surface, x, y, color=(0, 0, 0)):
    textDisplay = font.render(displayString, 1, color)
    textRect = textDisplay.get_rect()
    textRect.topleft = (x, y)
    surface.blit(textDisplay, textRect)

# DO NOT CHANGE ANYTHING INSIDE THIS FUNCTION


def run(width=500, height=500, caption=""):
    def redrawAllWrapper(data, screen):
        screen.fill(data.backgroundColor)
        redrawAll(screen, data)
        pygame.display.update()

    def keyDownWrapper(event, data, screen):
        keyDown(event, data)
        redrawAllWrapper(data, screen)

    def keyUpWrapper(event, data, screen):
        keyUp(event, data)
        redrawAllWrapper(data, screen)

    def mouseDownWrapper(event, data, screen):
        mouseDown(event, data)
        redrawAllWrapper(data, screen)

    def mouseUpWrapper(event, data, screen):
        mouseUp(event, data)
        redrawAllWrapper(data, screen)

    def timerFiredWrapper(data, screen):
        timerFired(data)
        redrawAllWrapper(data, screen)
    pygame.init()  # starts pygame
    pygame.display.set_caption(str(caption))

    class Struct():

        def __init__(self): return
    data = Struct()
    data.width = width
    data.height = height
    screen = pygame.display.set_mode((width, height))
    data.clock = pygame.time.Clock()
    data.backgroundColor = (0, 0, 0)
    data.timerDelay = 50
    init(data)
    global font
    font = pygame.font.SysFont(None, 36)
    redrawAllWrapper(data, screen)
    # Event handler
    while True:
        data.clock.tick(data.timerDelay)
        timerFiredWrapper(data, screen)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                keyDownWrapper(event, data, screen)
            elif event.type == KEYUP:
                keyUpWrapper(event, data, screen)
            elif event.type == MOUSEBUTTONDOWN:
                mouseDownWrapper(event, data, screen)
            elif event.type == MOUSEBUTTONUP:
                mouseUpWrapper(event, data, screen)

run()
