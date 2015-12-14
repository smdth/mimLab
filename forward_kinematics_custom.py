#!/usr/bin/env python

# This script should return the x y z and orientation coordinates of the end effector of the left limb.
# PLEASE ADD YOUR CODE WHERE INDICATED
# Avoid modifying the rest of the code if not necessary
#
# Authors: Stefano Pietrosanti - s.pietrosanti@pgr.reading.ac.uk
#          Guy Butcher

import rospy
import baxter_interface
import numpy
from geometry_msgs.msg import (
    PoseStamped,
    Pose,
    Point,
    Quaternion,
)

print("MIM tutorial: forward kinematics.")
# Initialising ROS node
rospy.init_node("SSE_forward_kinematics")

######################  INSERT YOUR CODE HERE
# Create a "Limb" instance called "left_arm" linked to Baxter's left limb

left_arm = baxter_interface.Limb('left')

# Create a "pose" variable which holds the output of endpoint_pose()

pose = left_arm.endpoint_pose()

######################



# Return pose
print("Endpoint coordinates:")
print("X: " + str(pose['position'].x))
print("Y: " + str(pose['position'].y))
print("Z: " + str(pose['position'].z))
print("Orientation: " + str(pose['orientation']))
