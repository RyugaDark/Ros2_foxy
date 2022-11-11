#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import random
# TODO # import Int64 message here
from example_interfaces.msg import Int32
     
class NumberPublisherNode(Node): # Write Class Name Here
    def __init__(self):
        super().__init__("Number_publisher") # Write Node Name Here
        # TODO 
        # create publisher here
        self.publisher_ = self.create_publisher(Int32, "number_publisher",10)
        # create timer here
        self.timer_ = self.create_timer(0.5, self.publish_number) 
        self.get_logger().info("Number Publisher has started!!")

    def publish_number(self):
        msg = Int32()
        tp = random.randint(1,10)
        msg.data = tp
        self.publisher_.publish(msg) 
        # TODO
        # create message msg of Int64 here
        # publish the message 
        self.get_logger().info(f"Submitted number is {msg.data}")

        
def main(args=None):
        rclpy.init(args=args)
        node = NumberPublisherNode() # Write Class Name Here
        rclpy.spin(node)
        rclpy.shutdown()
     
if __name__ == "__main__":
	main()