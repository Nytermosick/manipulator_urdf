#!/usr/bin/env python

import rclpy
from rclpy.node import Node
from rclpy.clock import Clock

from sensor_msgs.msg import JointState
from std_msgs.msg import Header
from builtin_interfaces.msg import Duration
import time


class MinimalPublisher(Node):
	def __init__(self):
		super().__init__('publisher')
		self.pub =\
		 self.create_publisher( JointState, '/joint_states', 10)
		 
time_stamp = Clock().now()
 

	

def grad_to_rad(grad):
	grad = float(grad)
	if grad >= 360:
		grad -= 360 * (grad // 360)
		
	elif grad <= -360:
		grad += 360 * (grad // 360)
		
	return grad * 3.14/180
		
		
def main(args=None):
	rclpy.init(args=args)
	
	publisher = MinimalPublisher()
	msg = JointState()
	msg.header = Header()
	msg.header.stamp = time_stamp.to_msg()
	msg.name = ['joint_platform_to_link1', 'joint_link2_to_link1', 'joint_link4_to_link3']
	
	joint_platform_to_link1 = 0.0
	joint_link2_to_link1 = 0.0
	joint_link4_to_link3 = 0.0
		   
	i = 0.0
	
	while i <= 3.0:
		msg.header.stamp = time_stamp.to_msg()
		msg.position = [joint_platform_to_link1, joint_link2_to_link1, joint_link4_to_link3]
		if -3.14 <= joint_platform_to_link1 <= 3.14:
			joint_platform_to_link1 += i
		if -3.14 <= joint_link2_to_link1 <= 3.14:
			joint_link2_to_link1 += i
		if -3.14 <= joint_link4_to_link3 <= 3.14:
			joint_link4_to_link3 += i
		
		print(i)
		publisher.pub.publish(msg)
		i += 0.1
		time.sleep(0.015)
		

if __name__ == '__main__':
    main()
