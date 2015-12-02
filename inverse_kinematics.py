#!/usr/bin/env python

# This script should move Baxter's left limb to the chosen coordinates.
# PLEASE ADD YOUR CODE WHERE INDICATED
# Avoid modifying the rest of the code if not necessary
#
# Authors:      Stefano Pietrosanti - s.pietrosanti@pgr.reading.ac.uk
#               Guy Butcher

import rospy
import baxter_interface
import numpy
import argparse
import struct
import sys
from geometry_msgs.msg import (
    PoseStamped,
    Pose,
    Point,
    Quaternion,
)
from std_msgs.msg import Header
from baxter_core_msgs.srv import (
    SolvePositionIK,
    SolvePositionIKRequest,
)



print("MIM tutorial: inverse kinematics.")
# Initialising ROS node
rospy.init_node("SSE_inverse_kinematics")


# Inverse kinematics
limb = "left"
ns = "ExternalTools/" + limb + "/PositionKinematicsNode/IKService"
iksvc = rospy.ServiceProxy(ns, SolvePositionIK)
ikreq = SolvePositionIKRequest()
hdr = Header(stamp=rospy.Time.now(), frame_id='base')
inputting = True

######################  INSERT YOUR CODE HERE
# Define the x y z coordinates and the orientation of the effector
# Insert the values:

o = [1,0,0,0]

if len(sys.argv) == 8:
    px = sys.argv[1]
    py = sys.argv[2]
    pz = sys.argv[3]
    o[0] = sys.argv[4]
    o[1] = sys.argv[5]
    o[2] = sys.argv[6]
    o[3] = sys.argv[7]
else:
    px = 1   # x coordinate
    py = 1   # y coordinate
    pz = 1   # z coordinate
    o[0] = 1 # orientation quaternion x coordinate
    o[1] = 1 # orientation quaternion y coordinate
    o[2] = 1 # orientation quaternion z coordinate
    o[3] = 1 # orientation quaternion w coordinate
# WARNING: there is more code to be inserted later on
#####################

hdr = Header(stamp=rospy.Time.now(), frame_id='base')

poses = {
        'left': PoseStamped(
                header=hdr,
                pose=Pose(
                        position=Point(
                                x = px,
                                y = py,
                                z = pz,
                        ),
                        orientation=Quaternion(
                                x = o[0],
                                y = o[1],
                                z = o[2],
                                w = o[3],
                        )
                ),
        ),
}

# Print the pose
print("Chosen pose:")
print(poses['left'])
ikreq.pose_stamp.append(poses['left'])

# Call the IK service
try:
        rospy.wait_for_service(ns, 5.0)
        resp = iksvc(ikreq)
except (rospy.ServiceException, rospy.ROSException), e:
        rospy.logerr("Service call failed: %s" %(e,))
        #return 1

# Test if the response is valid
if (resp.isValid[0]):
        print("Success - Valid Joint Solution Found:")
        print("Moving Joints to Solution")
        limb_joints = dict(zip(resp.joints[0].name, resp.joints[0].position))
        print("Joint angles:")
        print(limb_joints)

else:
        print("INVALID POSE - No Valid Joint Solution Found.")

###################  INSERT CODE HERE
# Create a "Limb" instance called "left_arm" linked to Baxter's left limb

left_arm = baxter_interface.Limb('left')

# Use the "move_to_joint_positions" or "set_joint_positions" function to set the joint angles to "limb_joints"

left_arm.move_to_joint_positions(limb_joints)

###################
