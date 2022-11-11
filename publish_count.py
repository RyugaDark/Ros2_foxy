#!/usr/bin/env python3
from .number_subscriber import NumberCounterNode
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64     
     
     
class numbercounter(Node): # Write Class Name Here
    def __init__(self):
        super().__init__("   ") # Write Node Name Here
        self.counter = 0
        # TODO
        # create a subscriber node to subscribe the number
        self.subscriber = self.create_subscription(Int64, 'number_publisher', self.callback_number,10)
        # create a publisher to publish the count value
        self.publishers = self.create_publisher(Int64, 'pubsub', 10)
        
        self.get_logger().info("Number Counter Node Started")
   
   
    def callback_number(self, msg):
        # TODO 
        # increment the counter as the msg is received
        # initialise the new message of type Int64 to publish the counter value
        # publish the counter value 
        self.counter +=msg.data
        new = Int64
        new.data = self.counter
        self.publish.publish(new)
        self.get_logger().info(str(self.counter))    
        
        
def main(args=None):
        rclpy.init(args=args)
        node = NumberCounterNode() # Write Class Name Here
        rclpy.spin(node)
        rclpy.shutdown()
     
if __name__ == "__main__":
	main()