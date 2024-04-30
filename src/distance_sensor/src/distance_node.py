import rospy
from sensor_msgs.msg import Range
# import custom message type for Relative Velocity
import HCSR04 # import our driver module

class HCSR04Wrapper(object):

    def __init__(self):
        self.min_range = 3
        self.max_range = 400
        self.fov = 0.26179938779915 # 15 degrees

        topic_name = rospy.get_param("")
        # self.ultrasonicPub = rospy.Publisher(topic_name, Range, queue_size=10)    # topic name defined by param in launch file
        # self.ultrasonicVelocityPub = rospy.Publisher('/ultrasonic/relative_velocity', Range, queue_size=10)

        # loading the driver
        self.ultrasonic_sensor = HCSR04(trig_pin, echo_pin)   # trigger, echo

        self.rate = rospy.Rate(10) # 10hz
        rospy.Timer(self.rate, self.publish_current_distance)
        # rospy.Timer(self.rate, self.publish_current_velocity)

    def publish_current_distance(self):
        distance = self.ultrasonic_sensor.distance()

        message_str = "Distance: %s cm" % distance
        rospy.loginfo(message_str)
        
        #for distance in ranges:
        r = Range()

        r.header.stamp = rospy.Time.now()
        r.header.frame_id = "/base_link"
        r.radiation_type = Range.ULTRASOUND
        r.field_of_view = self.fov # 15 degrees
        r.min_range = self.min_range
        r.max_range = self.max_range

        r.range = distance
            
        self.ultrasonicPub.publish(r)

    def publish_current_velocity(self):
        relative_velocity = self.ultrasonic_sensor.speed()

        message_str = " Speed: %s m/s" % relative_velocity
        rospy.loginfo(message_str)
        
        rv = Range() # using range instead of a custom message type

        rv.header.stamp = rospy.Time.now()
        rv.header.frame_id = "/base_link"
        rv.radiation_type = Range.ULTRASOUND
        rv.field_of_view = self.fov
        rv.min_range = self.min_range
        rv.max_range = self.max_range

        rv.rage = relative_velocity # using range instead of a custom message type with a field relative velocity
            
        self.ultrasonicVelocityPub.publish(rv)

    def stop(self):
        self.ultrasonicPub.unregister()
        self.ultrasonicVelocityPub.unregister()

# Main function.
if __name__ == '__main__':
    # Initialize the node and name it.
    rospy.init_node("ultrasonic_driver", anonymous=False)

    ultrasonic_wrapper = HCSR04Wrapper()

    rospy.on_shutdown(ultrasonic_wrapper.stop)
    rospy.loginfo("Ultrasonic driver is now started.")

    rospy.spin()