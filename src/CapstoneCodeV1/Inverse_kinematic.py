import numpy as np
import matplotlib.pyplot as plt
import math

def IK(y, gribber_angle,L1=4.5,L2=6.3,L3=7,Base_Height = 5):
    #L1-Arm L2-elbow L3-wrist Base is distance from elbow joint to robot rotation center
	#usage: only get input for target height and the gripper angle, the height should adjust automatically
    pi = np.pi
    gribber_angle = np.deg2rad(gribber_angle)
    y = y - Base_Height #reduce base height
    y = y - np.sin(gribber_angle)*L3
    if y > L1 + L2:
        print("too far")
        y = L1 + L2 - 0.01
    if(y > L1):
        theta1 = pi/2
        y = y - L1
        theta2 = -np.arccos(y/L2)
    else:
        theta1 = np.arcsin(y/L1)
        theta2 = -theta1
    
    theta3 = gribber_angle - theta1 - theta2
    return theta1,theta2,theta3

def plot_arm(theta1, theta2, theta3, L1, L2, L3):
    # for testing, don't use this in controlling code(will stuck)
    # theta1 = np.deg2rad(theta1)
    # theta2 = np.deg2rad(theta2)
    # theta3 = np.deg2rad(theta3)

    joint1_x, joint1_y = L1 * math.cos(theta1), L1 * math.sin(theta1)
    joint2_x, joint2_y = joint1_x + L2 * math.cos(theta1 + theta2), joint1_y + L2 * math.sin(theta1 + theta2)
    end_effector_x, end_effector_y = joint2_x + L3 * math.cos(theta1 + theta2 + theta3), joint2_y + L3 * math.sin(theta1 + theta2 + theta3)

    plt.figure()
    plt.plot([0, joint1_x], [0, joint1_y], 'ro-')  
    plt.plot([joint1_x, joint2_x], [joint1_y, joint2_y], 'go-')  
    plt.plot([joint2_x, end_effector_x], [joint2_y, end_effector_y], 'bo-')  
    plt.plot(end_effector_x, end_effector_y, 'ko')  

    plt.xlim(-L1-L2-L3, L1+L2+L3)
    plt.ylim(-L1-L2-L3, L1+L2+L3)
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.title('3-DOF Arm Configuration')
    plt.grid(True)
    plt.axis('equal')
    plt.show()



def main():
    try:
        user_input = input("get input, separate by space\n")

        elements = user_input.split(' ')
        L1 = 4.5
        L2 = 6.3
        L3 = 7
        parsed_elements = [float(element.strip()) for element in elements]
        result = IK(parsed_elements[0],parsed_elements[1],L1=L1,L2=L2,L3=L3)
        result = np.array(result)
        plot_arm(result[0], result[1], result[2], L1, L2, L3)
        print("theta_base,theta1,theta2,theta3:", result*180/np.pi)
    except ValueError:
        print("input is not valid number")
    except IndexError:
        print("input at least 2")

if __name__ == '__main__':
    try:

        while 1:
            main()
    except KeyboardInterrupt:
        print('Execution Aborted By User')
