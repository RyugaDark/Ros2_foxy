#!/usr/bin/env python3
from pickle import TRUE
import rclpy
from rclpy.node import Node
# TODO
# use SetBool service
from example_interfaces.srv import SetBool
# use Int32   
from example_interfaces.msg import Int32
     
class NumberCounterNode(Node):
    def __init__(self):
        super().__init__("reset_counter")
        self.counter = 0
        # TODO
        # create publisher
        self.publisher_ = self.create_publisher(Int32, "number_count",10)
        # create subscriber
        self.subscriber = self.create_subscription(Int32, 'number_publisher', self.callback_number,10)
        # create service 
        self.server_ = self.create_service(SetBool, "number_reset",self.callback_reset_counter) 
        self.get_logger().info("Counter Node started")
   
   
    def callback_number(self, msg):
        # TODO
        # increment counter
        # publish the counter value
        # print the counter value
        self.get_logger().info(str(self.counter))
        self.counter +=msg.data
        new = Int32()
        new.data = self.counter

       
        
    def callback_reset_counter(self, request, response):
        # TODO
        if request.data == True:
            self.counter = 0
            response.success = True
            self.get_logger().info("Reset Successful")
        
        
        return response
    
    
def main(args=None):
        rclpy.init(args=args)
        node = NumberCounterNode() 
        rclpy.spin(node)
        rclpy.shutdown()
     
if __name__ == "__main__":
	main()