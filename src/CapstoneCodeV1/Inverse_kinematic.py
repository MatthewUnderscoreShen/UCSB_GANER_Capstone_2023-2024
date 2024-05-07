import numpy as np
import matplotlib.pyplot as plt
import math

def IK(x ,y ,z=0,L1=4.5,L2=6.3,L3=7,Base=4.5,gribber_angle = 0, Base_Height = 5,currentBase = 0):
    #L1-Arm L2-elbow L3-wrist Base is distance from elbow joint to robot rotation center
	#usage: get relative x y z cordinate with origin of robot,return required arm angle
    #note1: x point to front, y point to up, z point to right(turning position)
    #note2: theta base is the angle that body need to rotate for z position
    #note3: for now, ignore moving the body, but can add if necessary
    #note4: gripper is special arm, we need to fix the absolute angle, default is horizontal
    currentBase = np.deg2rad(currentBase)
    y = y - Base_Height
    gribber_angle = np.deg2rad(gribber_angle)
    theta_base = np.arctan2(z,x+Base)
    x_actual = np.sqrt(z**2 + x**2) - Base
    x_3= x-np.cos(gribber_angle)*L3
    y_3= y-np.sin(gribber_angle)*L3
    D = math.sqrt(x_3**2 + y_3**2)
    if D > L1 + L2:
        print("too far")
        x_3 = math.sqrt((L1+L2)**2 - y_3**2) - 0.01
    if D < np.abs(L1-L2):
        print("too close")
        return None

    theta2 = -np.arccos((x_3**2 + y_3**2 - L1**2 - L2**2) / (2 * L1 * L2))
    theta1 = np.arctan2(y_3, x_3) - np.arctan2(L2 * np.sin(theta2), L1 + L2 * np.cos(theta2))
    theta3 = gribber_angle-theta2-theta1
    
    return theta_base-currentBase,theta1,theta2,theta3

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
        result = IK(parsed_elements[0],parsed_elements[1],z = parsed_elements[2],L1=L1,L2=L2,L3=L3,gribber_angle=parsed_elements[3],currentBase = parsed_elements[4])
        result = np.array(result)
        plot_arm(result[1], result[2], result[3], L1, L2, L3)
        print("theta_base,theta1,theta2,theta3:", result*180/np.pi)
    except ValueError:
        print("input is not valid number")
    except IndexError:
        print("input at least 5")

if __name__ == '__main__':
    try:

        while 1:
            main()
    except KeyboardInterrupt:
        print('Execution Aborted By User')
