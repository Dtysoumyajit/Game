import sys
import random as r
import pygame
from pygame.locals import *

pygame.init()
x,x1,x2,x3=0,250,600,480
y,y1,y2,y3=0,300,700,900
n=0
s=.2
s1,s2,s3,s4=0,0,0,0
h1,h2,h3,h4=0,0,0,0
a,a1,a2,a3=0,0,0,0
b,b1,b2,b3=0,0,0,0
surface = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
surfrect = surface.get_rect()
rect = pygame.Rect((0, 0), (128, 128))
rect1=pygame.Rect((x,y),(128,128))
rect2=pygame.Rect((x1,y1),(256,128))
rect3=pygame.Rect((x2,y2),(64,128))
rect4=pygame.Rect((x3,y3),(256,256))
rect.center = (surfrect.w / 2, surfrect.h / 2)
touched = False
run=True
hp=720
dec=2
w=surface.get_width()
h=surface.get_height()
def obstacle1():
	surface.fill((150,100,50),rect1)
def obstacle2():
	surface.fill((150,100,50),rect2)
def obstacle3():
	surface.fill((150,100,50),rect3)
def obstacle4():
	surface.fill((150,100,50),rect4)
def hpbar(x):
	recth=pygame.Rect((0,0),(x,20))
	surface.fill((50,100,100),recth)
while run:
    rect1=pygame.Rect((x,y),(100,100))
    rect2=pygame.Rect((x1,y1),(100,100))
    rect3=pygame.Rect((x2,y2),(100,100))
    rect4=pygame.Rect((x3,y3),(100,100))
   
    if rect1.left<=0 and n>0 and h1>0:
    	a=5+s1
    	s1+=s
    	h1=1
    if rect1.right>=w and n>0 and h1>0:
    	a=-1*(5+s1)
    	s1+=s
    	h1=1
    if rect1.top<=0 and n>0 and h1>0:
    	b=5+s1
    	s1+=s
    	h1=1
    if rect1.bottom>=h and n>0 and h1>0:
    	b=-1*(5+s1)
    	s1+=s
    	h1=1
    if h1<1 and n>0:
    	a=5
    	b=5
    	h1=1
    x+=a
    y+=b
    
    if rect2.left<=0 and n>0 and h2>0:
    	a1=5+s2
    	s2+=s
    	h2=1
    if rect2.right>=w and n>0 and h2>0:
    	a1=-1*(5+s2)
    	s2+=s
    	h2=1
    if rect2.top<=0 and n>0 and h2>0:
    	b1=5+s2
    	s2+=s
    	h2=1
    if rect2.bottom>=h and n>0 and h2>0:
    	b1=-1*(5+s2)
    	s2+=s
    	h2=1
    if h2<1 and n>0:
    	a1=5
    	b1=5
    	h2=1
    x1+=a1
    y1+=b1
    
    if rect3.left<=0 and n>0 and h3>0:
    	a2=5+s3
    	s3+=s
    	h3=1
    if rect3.right>=w and n>0 and h3>0:
    	a2=-1*(5+s3)
    	s3+=s
    	h3=1
    if rect3.top<=0 and n>0 and h3>0:
    	b2=5+s3
    	s3+=s
    	h3=1
    if rect3.bottom>=h and n>0 and h3>0:
    	b2=-1*(5+s3)
    	s3+=s
    	h3=1
    if h3<1 and n>0:
    	a2=5
    	b2=5
    	h3=1
    x2+=a2
    y2+=b2
    
    if rect4.left<=0 and n>0 and h4>0:
    	a3=5+s4
    	s4+=s
    	h4=1
    if rect4.right>=w and n>0 and h4>0:
    	a3=-1*(5+s4)
    	s4+=s
    	h4=1
    if rect4.top<=0 and n>0 and h4>0:
    	b3=5+s4
    	s4+=s
    	h4=1
    if rect4.bottom>=h and n>0 and h4>0:
    	b3=-1*(5+s4)
    	s4+=s
    	h4=1
    if h4<1 and n>0:
    	a3=5
    	b3=5
    	h4=1
    x3+=a3
    y3+=b3
    
    for ev in pygame.event.get():
        if ev.type == QUIT:
            pygame.quit()
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            if rect.collidepoint(ev.pos):
                touched = True
                n=1
                pygame.mouse.get_rel()
        elif ev.type == pygame.MOUSEBUTTONUP:
            touched = False
    clock.tick(100)
    surface.fill((7, 199, 199))
    if touched:
        rect.move_ip(pygame.mouse.get_rel())
        rect.clamp_ip(surfrect)
        
    if rect.colliderect(rect1) or rect.colliderect(rect2) or rect.colliderect(rect3) or rect.colliderect(rect4):
    	hp=hp-dec
    	if hp==0:
    		run=False
    	
    if rect.left<=0 or rect.right>=w or rect.top<=0 or rect.bottom >=h:
    	run =False
    	
    surface.fill((5, 99, 99), rect)
    
    obstacle1()
    obstacle2()
    obstacle3()
    obstacle4()
    hpbar(hp)
    pygame.display.flip()

