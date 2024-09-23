#!/usr/bin/env python

import rclpy
import time
from rclpy.node import Node

from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from std_msgs.msg import Header
from builtin_interfaces.msg import Duration


class MinimalPublisher(Node):
	def __init__(self):
		super().__init__('publisher')
		self.pub =\
		 self.create_publisher(JointTrajectory, 'iiwa_arm_controller/joint_trajectory', 1)
	

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
	msg = JointTrajectory()
	msg.header = Header()
	msg.joint_names = ['joint_a1', 'joint_a2', 'joint_a3',\
					   'joint_a4', 'joint_a5', 'joint_a6', 'joint_a7']
					   
	duration_sec = 2
	duration_nanosec = 0.5
					   
	dots = JointTrajectoryPoint()
	dots.time_from_start = Duration(sec=int(duration_sec),\
									nanosec=int(duration_nanosec))
	#dots.positions = [0.785, 0.0, 0.785, 0.785, 0.785, 0.785, 0.785]
	
	while True:
		print('\nPlease, write 7 angles for each joint')
		pos_digits = list(map(grad_to_rad, input().split()))
		if len(pos_digits) != 7:
			print('\nPlease, write 7 angles for each joint')
			continue
	
		dots.positions = pos_digits
		msg.points = [dots]
		publisher.get_logger().info(f'\nPublishing...\n{pos_digits}')
		time.sleep(1)
		publisher.pub.publish(msg)
		

if __name__ == '__main__':
    main()
