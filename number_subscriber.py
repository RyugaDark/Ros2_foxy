#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
# TODO # import Int64 message here
  


class NumberCounterNode(Node): # Write Class Name Here
    def __init__(self):
        super().__init__("counter")  # Write Node Name Here
        self.counter = 0
        # TODO 
        # create subscriber here with callback function name callback_number
        self.subscriber_ = self.create_subscription(Int64, "number_publisher", self.callback_number, 10)
        
        self.get_logger().info("Subscriber Node started")
   
   
    def callback_number(self, msg):
        # TODO 
        #increment the counter as the data is received from publisher node
        self.get_logger().info(str(self.counter))
        self.counter +=msg.data
        new = Int64()
        new.data = self.counter
           
        
        
def main(args=None):
        rclpy.init(args=args)
        node = NumberCounterNode() # Write Class Name Here
        rclpy.spin(node)
        rclpy.shutdown()
     
if __name__ == "__main__":
	main()