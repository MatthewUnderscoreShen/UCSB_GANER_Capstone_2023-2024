import xarm

class Arm(object):

    def __init__(self):
        self.robot = self.connect_to_robot()
        if self.robot is None:
            print("Exiting program.")
            exit()
        print(self.robot)
    
    """
    IK control plan:
        use Dpad
        imagine xyz from back of robot perspective
            x is horizontal (locked)
            y is vertical
            z is depth
        up down = y axis
            up = up
            lmao
        left right = z axis
            left = back (towards back of bot)
            right = forwards
    """
    
    def set_pos(self, angles):  # 5 links
        # old code says -125 to 125 deg range
        # Limits
        # The ugly if statements are like "danger zone" limits. 
        # The limits become more stringent if a lower link is at an extreme
        # It's basically to prevent the arm from smacking the Pi
        # or the ground
        # This would be easier with IK

        # can change
        self.robot.setPosition(1, min(750,max(400,angles[0])), wait=False)
        # can change
        self.robot.setPosition(2, min(800,max(50,angles[1])), wait=False)
        self.robot.setPosition(3, min(850,max(150,angles[2])), wait=False)
        self.robot.setPosition(4, min(880,max(150,angles[3])), wait=False)
        # link 1: 500 limit (vertical)
        self.robot.setPosition(5, min(800,max(500,angles[4])), wait=False) 
    
    def get_pos(self):      # returns angle array in deg
        # Doesn't work because xarm sucks
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