import xarm

class Arm(object):

    def __init__(self):
        self.robot = self.connect_to_robot()
        if self.robot is None:
            print("Exiting program.")
            exit()
        print(self.robot)
    
    def set_pos(self, angles):  # 5 links
        # old code says -125 to 125 deg range
        self.robot.setPosition(1, angles[0], 500)
        self.robot.setPosition(2, angles[1], 500)
        self.robot.setPosition(3, angles[2], 500)
        self.robot.setPosition(4, angles[3], 500)
        self.robot.setPosition(5, angles[4], 500)
    
    def get_pos(self):      # returns angle array in deg
        return [self.robot.getPosition(1, degrees=True),
                self.robot.getPosition(2, degrees=True),
                self.robot.getPosition(3, degrees=True),
                self.robot.getPosition(4, degrees=True),
                self.robot.getPosition(5, degrees=True)]

    def connect_to_robot(self):
        try:
            arm = xarm.Controller("USB")
            return arm
        except:
            print("Unable to connect to arm.")
            return None