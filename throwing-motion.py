import math as mt
import matplotlib.pyplot as plt
import numpy as np
#without drag
l_x1=[]
l_y1=[]
speed_0=float(input('please enter frist speed to (m/s):'))
angle=float(input('please enter frist angle to (rad):'))
angle_0=mt.radians(angle)
time=0
length_y=0
H1=((speed_0**2)*((mt.sin(angle_0))**2))/(2*9.81)
R1=((speed_0**2)*(mt.sin(2*angle_0)))/9.81
while length_y>=0:
    speed_x1=(speed_0*mt.cos(angle_0))*time
    speed_y1=-(9.81*time)+(speed_0*mt.sin(angle_0))
    length_x=(speed_0*mt.cos(angle_0))*time
    l_x1.append(length_x)
    length_y=-(0.5*9.81*(time**2))+((speed_0*mt.sin(angle_0))*time)
    l_y1.append(length_y)
    time+=0.0001
#-----------------------------------------------------------------------
#with drag
l_x=[]
l_y=[]
Area=float(input('please enter area to (m^2):'))
ρ=float(input('please enter particle ρ to (kg/m^3):'))
C=float(input('please enter Cd for shape:'))
mass=float(input('please enter particle mass to (kg):'))
k=(Area*ρ*C)/2
speed_x=speed_0*mt.cos(angle_0)
speed_y=speed_0*mt.sin(angle_0)
time1=0
length_y1=0
length_x1=0
while length_y1>=0:
    acceleration_x=-(k*(((speed_x**2)+(speed_y**2))**0.5)*speed_x)/mass
    acceleration_y=-9.81-(k*(((speed_x**2)+(speed_y**2))**0.5)*speed_y)/mass
    speed_x+=acceleration_x*0.0001
    speed_y+=acceleration_y*0.0001
    length_x1=length_x1+(speed_x*0.0001)
    l_x.append(length_x1)
    length_y1=length_y1+(speed_y*0.0001)
    l_y.append(length_y1)
    if length_y1<0:
        L=length_x1
    if -0.001<speed_y<0.001:
        M=length_y1
    time1+=0.0001
print(length_y)
print(f'time without drag force is {time}s')
print(f'maximum heith without drag force is {H1} and maximum length is {R1}')
print(length_y1)
print(f'time with drag force is {time1}s')
print(f'maximum heith with drag force is {M} and maximum length is {L}')
plt.plot(l_x1,l_y1,'r-',label='without drag force')
plt.plot(l_x,l_y,'g-',label='with drag force')
plt.xlabel('x axis (m)')
plt.ylabel('y axis (m)')
plt.title('particle action')
plt.show()