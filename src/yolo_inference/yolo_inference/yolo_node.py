import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
from ultralytics import YOLO
from rclpy.qos import qos_profile_sensor_data

class YOLONode(Node):
    def __init__(self):
        super().__init__('yolo_node')
        self.bridge = CvBridge()
        self.model = YOLO("/home/daksh/ros2_ws/src/yolo_inference/yolo_inference/best.pt") 


        # Subscribe to image topic with compatible QoS
        self.image_subscriber = self.create_subscription(
            Image,
            '/robot1/zed2i/left/image_rect_color',  # Topic from .db3 file
            self.image_callback,
            qos_profile_sensor_data  
        )

        # Publisher for annotated images
        self.image_publisher = self.create_publisher(
            Image,
            '/yolo/annotated_image',
            10)

    def image_callback(self, msg):
        # Convert ROS Image message to OpenCV format
        frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

        # Perform YOLO inference on the frame
        results = self.model(frame)
        annotated_frame = results[0].plot()

        # Publish the annotated image back as a ROS topic
        annotated_msg = self.bridge.cv2_to_imgmsg(annotated_frame, encoding='bgr8')
        self.image_publisher.publish(annotated_msg)

def main(args=None):
    rclpy.init(args=args)
    node = YOLONode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

