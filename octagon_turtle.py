#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import time
import math

  
  
class TurtleControllerNode(Node):
    def __init__(self):
        super().__init__("turtle_controller")
        self.target_x = 4.0
        self.target_y = 6.0
        self.pose = None
        self.pub_vel = self.create_publisher(Twist, "turtle1/cmd_vel", 10)
        self.timer = self.create_timer(0.01, self.control_loop)
    
    def control_loop(self):
        msg = Twist()
        
        msg.linear.x = 2.0
        time.sleep(1)
        self.pub_vel.publish(msg) 
        #time.sleep(1)
        msg.linear.x = 0.0
        time.sleep(1)
        self.pub_vel.publish(msg)        
        msg.angular.z = 0.7853981634
        time.sleep(1)
        self.pub_vel.publish(msg)

    
def main(args=None):
    rclpy.init(args=args)
    node = TurtleControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()
    
       
if __name__ == "__main__":
	main()
