#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

# Global variable to hold the latest image
cv_image = None

def image_callback(msg):
    global cv_image

    try:
        # Convert the ROS Image message to OpenCV format
        bridge = CvBridge()
        cv_image = bridge.imgmsg_to_cv2(msg, "bgr8")
        # You can also process the image data here as needed
        # ...

    except Exception as e:
        rospy.logerr(e)

def main():
    rospy.init_node('video_subscriber_node', anonymous=True)

    # Subscribe to the "/kubot_cam/image_raw" topic
    rospy.Subscriber("/kubot_cam/image_raw", Image, image_callback)

    # Set the rate at which you want to display images (e.g., 10 Hz)
    rate = rospy.Rate(10)  # 10 Hz

    print("Press 'q' to quit.")
    while not rospy.is_shutdown():
        # Display the image using OpenCV
        if cv_image is not None:
            cv2.imshow("Live Stream", cv_image)

        key = cv2.waitKey(1) & 0xFF

        # Quit on 'q' key press
        if key == ord('q'):
            break

        rate.sleep()

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
