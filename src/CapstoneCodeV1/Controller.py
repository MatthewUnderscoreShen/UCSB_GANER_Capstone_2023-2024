"""
new_controller.py
Modified by Xiangying Zuo

Modifications:
1. Add comments and made the code more readable

----------------------------------------------------------------
-------Action required in Pi Terminal-------------------------
    > sudo apt-get -y install jd
  #Install Ds4:
    > sudo pip3 install ds4drv
    > sudo wget https://raw.githubusercontent.com//chrippa/ds4drv/master/udev/50-ds4drv.rules -O /etc/udev/rules.d/50-ds4drv.rules
    > sudo udevadm control --reload-rules
    > sudo udevadm trigger
    > sudo nano /etc/rc.local
    # add next line after # By default this script does nothing
    > /usr/local/bin/ds4drv &
    control o
    control x
then connect via bluetooth
-----------------------------------------------------------------
"""

import pygame
from time import sleep
from os import environ

# Initialize pygame and joystick
pygame.init()
controller = pygame.joystick.Joystick(0)
controller.init()

### Define button mappings
#"x,o,t,s" are pins for function buttons: x -cross, o - circle, t - triangle, s - square
#'axis1' is horizontal position of left joystick ,'axis2' is vertical position of left joystick, 'axis3' horizontal of right,'axis4' vertical of right
buttons = {'x':0.,'o':0.,'t':0.,'s':0.,'L1':0.,'R1':0.,'L2':0.,'R2':0.,'share':0.,'options':0.,
           'axis1':0.,'axis2':0.,'axis3':0.,'axis4':0.,'Dpad up':0,'Dpad down':0, 'Dpad left':0,'Dpad right':0}

# Define initial axis values
axiss = [0.,0.,-1.,0.,0.,-1.]

# Set display for pygame
environ['DISPLAY'] = ':0'
pygame.display.init()

# Define function to get joystick values
def getJS(name=''):
    global buttons,axiss
    
    # Retrieve any events
    use_joystick = False
    for event in pygame.event.get():                                 # Analog Sticks
        # If joystick is moved
        if event.type == pygame.JOYAXISMOTION:
            axiss[event.axis] = round(event.value,2)
        
        # If button is pressed
        elif event.type == pygame.JOYBUTTONDOWN:                     # When Button pressed
            for x,(key,val) in enumerate(buttons.items()):
                if x < 10:
                    if controller.get_button(x):
                        buttons[key] = 1
        
        # if button is released 
        elif event.type == pygame.JOYBUTTONUP:                       # When Button released
#             print(event.dict,event.joy,event.button,'RELEASED')
            for x,(key,val) in enumerate(buttons.items()):
                if x < 10:
                    if event.button == x:
                        buttons[key] = 0
        
        # if directional buttons (Dpad) were pressed 
        elif event.type == pygame.JOYHATMOTION:
            hat = controller.get_hat(event.hat)  	# return position for hat (x,y) for x,y in -1, 0, 1
            for x,(key,val) in enumerate(buttons.items()):
                if x == 14 or x == 15:
                    if hat[1] > 0:
                        buttons['Dpad up'] = hat[1]
                    else:
                        buttons['Dpad up'] = 0
                    if hat[1] < 0:
                        buttons['Dpad down'] = abs(hat[1])
                    else:
                        buttons['Dpad down'] = 0
                if x == 16 or x == 17:
                    if hat[0] > 0:
                        buttons['Dpad right'] = hat[0]
                    else:
                        buttons['Dpad right'] = 0
                    if hat[0] < 0:
                        buttons['Dpad left'] = abs(hat[0])
                    else:
                        buttons['Dpad left'] = 0

    # to remove element 2 since axis numbers are 0 1 3 4
    buttons['axis1'], buttons['axis2'], buttons['axis3'], buttons['axis4'], buttons['L2'], buttons['R2']= [axiss[0],axiss[1],axiss[3],axiss[4], axiss[2], axiss[5]]

    if name == '':
        return buttons
    else:
        return buttons[name]

def main():
    print(getJS())
    sleep(0.1)

if __name__ == '__main__':
    while True:
        main()