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
	
		
def main(args=None):
	rclpy.init(args=args)
	
	publisher = MinimalPublisher()
	msg = String()
	
	while True:
		msg.data = input()
		if msg.data == 'quit':
			publisher.destroy_node()
			rclpy.shutdown()
			
		publisher.get_logger().info(f'Publishing: {msg.data}')
		time.sleep(1)
		publisher.publisher_.publish(msg)
		

if __name__ == '__main__':
    main()
