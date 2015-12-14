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

if len(sys.argv) > 1:
    px = sys.argv[1]
    py = sys.argv[2]
    pz = sys.argv[3]
    o[0] = sys.argv[4]
    o[1] = sys.argv[5]
    o[2] = sys.argv[6]
    o[3] = sys.argv[7]
 
else:

    px = 0.704303194185
    py = -0.0689719359237
#    pz = 0.0323706170901

    px = 0.52
    py = 0
    pz = 0.4
    #pz = 0.5
    px,py,pz = 0.75711104, -0.169506  ,  0.11665723

    o[0] = 0.75989153540926047
    o[1] = 0.56884166656018065
    o[2] = 0.024265470161950277
    o[3] = 0.31368009142470676
    #o[3] = [0.024265470161950277, 0.31368009142470676, 0.75989153540926047, 0.56884166656018065]
#    o[0] = 0.8123874156885869
#    o[1] = 0.4683948692594124
#    o[2] = 0.02062197493607546
#    o[3] = 0.3467097740647253

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
