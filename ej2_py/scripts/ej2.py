#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Int16

def callback(msg):
    rospy.loginfo("mensaje recibido: %s",msg.data)

def memory_subscriber():
    rospy.init_node('suscriptor_ej2',anonymous=True)
 #el primer argumento, es el nombrel del topic al que queremos suscribirnos...
 #el segundo argumento es el tipo de mensaje,
    rospy.Subscriber('contador',Int16,callback)
    rospy.spin()

if __name__ == "__main__":
    try:
        memory_subscriber()
    except rospy.ROSInterruptException:
        pass 
