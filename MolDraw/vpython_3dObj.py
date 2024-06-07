from vpython import *
from numpy import random


'''
ball1 = sphere(pos=vector(1,2,1),
                radius=0.5)

ball2 = sphere(pos=vector(4,2,1),
                radius=1.5)'''


#ball = sphere(pos=vector(-5,0,0), radius=0.5,color=color.cyan)
#wallR = box(pos=vector(6,0,0), size=vector(0.2,12,12), color=color.green)
#ball.velocity = vector(25,0,0)
N_frame = 100
N_balls = 5
t_end = 1

deltat = t_end/N_frame
t = 0
i = 0
#pos = random.randint(10, size=(N_balls,3))
#print(tuple(pos[0]))
'''
#ball.pos = ball.pos + ball.velocity*deltat
if ball.pos.x > wallR.pos.x:
         ball.velocity.x = -ball.velocity.x
     ball.pos = ball.pos + ball.velocity*deltat
'''
#ball = sphere(pos=vector(-5,0,0), radius=0.5,color=color.cyan)

balls = [sphere(pos=vector(-i,0,0), radius=0.5,color=color.cyan) for i in range(N_balls)]
while t < t_end:
    rate(100)
    #print(i+1)
    for ball in balls:
        ball.pos = ball.pos + vec.random()
    '''
    #scene = canvas(title=f'Frame = {i+1}')
    pos = random.randint(10, size=(N_balls,3))
    radii = random.rand(10)
    for i in range(N_balls):
        #p = pos[i]
        #ball = sphere(pos=vector(p[0],p[1],p[2]), radius=radii[i],color=color.cyan)
        star = sphere(pos=vec.random(), make_trail=True, retain=150)
        
    '''
    t = t + deltat 
    i += 1
    
    
