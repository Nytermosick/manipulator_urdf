#!/usr/bin/env python

import rclpy
import time
from rclpy.node import Node

from trajectory_msgs.msg import JointTrajectory
from std_msgs.msg import String


class MinimalPublisher(Node):
	def __init__(self):
		super().__init__('publisher')
		self.publisher_ = self.create_publisher(String, 'topic', 1)
		timer_period = 1
		self.timer = self.create_timer(timer_period, self.timer_callback)
		self.i = 0
		
	def timer_callback(self):
		msg = String()
		msg.data = f'Testing {self.i}'
		self.publisher_.publish(msg)
		self.get_logger().info(f'Publishing: {msg.data}')
		self.i += 1
		
def main(args=None):
	rclpy.init(args=args)
	
	publisher = MinimalPublisher()
	
	rclpy.spin(publisher)
	
	minimal_publisher.destroy_node()
	rclpy.shutdown()
		

if __name__ == '__main__':
    main()
