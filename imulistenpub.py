import rclpy
from rclpy.node import Node

from sensor_msgs.msg import LaserScan
from std_msgs.msg import String #import string from std msgs

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import MagneticField,Imu
from std_msgs.msg import Float64
from diagnostic_msgs.msg import DiagnosticStatus
from rcl_interfaces.msg import ParameterDescriptor

from math import isnan

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('IMU_subscriber')
        self.subscription = self.create_subscription(
            Imu,
            'geo_raw',
            self.listener_callback,
            10)
        self.cmd_pub_2=self.create_publisher(String, "/compasstopic", 10)
        self.subscription  # prevent unused variable warning
        
        self.get_logger().info("IMU Subscriber initiated")

    def listener_callback(self, msg):
        # Find smallest value
        txt2 = String()
            	
        # Log info
        self.get_logger().info('w: "%s"' % msg.orientation.w)
        self.get_logger().info('x: "%s"' % msg.orientation.x)
        self.get_logger().info('y: "%s"' % msg.orientation.y)
        self.get_logger().info('z: "%s"' % msg.orientation.z)
        
        if msg.orientation.x <-1 :
        	        self.get_logger().info('You are tipping left: "%s"' % msg.orientation.x)
        if msg.orientation.x > 1 :
        	        self.get_logger().info('You are tipping right: "%s"' % msg.orientation.x)
        if msg.orientation.y <0.15:
        		self.get_logger().info('You are tipping backwards:"%s"' %msg.orientation.y)
        if msg.orientation.y >0.4:
        		self.get_logger().info('You are tipping forwards:"%s"' %msg.orientation.y)
        if msg.orientation.w > 3.50:
        		self.get_logger().info('You are facing North:"%s"' %msg.orientation.w)
        		#txt2 = String()
        		txt2.data = "Facing North"
        		self.cmd_pub_2.publish(txt2) #was self.cmd_pub_2 
        		
        if msg.orientation.w > 2.70 and msg.orientation.w < 3.10 :
        		self.get_logger().info('You are facing West:"%s"' %msg.orientation.w)
        		txt3 = String()
        		txt3.data = "Facing West"
        		self.cmd_pub_2.publish(txt3) #was self.cmd_pub_2
        if msg.orientation.z < -3.00 and msg.orientation.z > -3.05 :
        		self.get_logger().info('You are facing East:"%s"' %msg.orientation.z)
        		txt4 = String()
        		txt4.data = "Facing East"
        		self.cmd_pub_2.publish(txt4) #was self.cmd_pub_2
       # if msg.orientation.z > 3.60: #and msg.orientation.z < -3.90 :
        #		self.get_logger().info('You are facing South:"%s"' %msg.orientation.z)
        if msg.orientation.w < 0.88 and msg.orientation.w > 0.30 :
        		self.get_logger().info('You are facing South:"%s"' %msg.orientation.z)
        		txt5 = String()
        		txt5.data = "Facing South"
        		self.cmd_pub_2.publish(txt5) #was self.cmd_pub_2
        
        	

def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()
    

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
