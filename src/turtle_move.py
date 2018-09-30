#!/usr/bin/env python

import sys
import rospy
from geometry_msgs.msg import Twist

def turtle_move(speed, distance, isForward):
    #distance = speed * time
    speed_pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    twist = Twist()

    if isForward: twist.linear.x = abs(speed)
    else: twist.linear.x = -abs(speed)
    twist.linear.y = 0
    twist.linear.z = 0

    twist.angular.x = 0
    twist.angular.y = 0
    twist.angular.z = 0

    t0 = rospy.get_time()
    curr_distance = 0

    while curr_distance < distance:
        t1 = rospy.get_time()
        curr_distance = speed * (t1-t0)
        speed_pub.publish(twist)
        rate.sleep()

    twist.linear.x = 0
    speed_pub.publish(twist)

def usage():
    return '%s [speed distance isForward]'%sys.argv[0]

if __name__ == '__main__':
    if len(sys.argv) == 4:
        speed = float(sys.argv[1])
        distance = float(sys.argv[2])
        isForward = int(sys.argv[3])
    else:
        print usage()
        sys.exit(1)
    try:
        turtle_move(speed, distance, isForward)
    except rospy.ROSInterruptException:
        pass