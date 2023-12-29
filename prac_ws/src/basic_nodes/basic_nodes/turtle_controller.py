import rclpy
import random
from rclpy.node import Node 
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist


class Turtle_Controller(Node):

    def __init__(self):
        super().__init__("turtle_controller")

        self.pose_subscr = self.create_subscription(
            Pose, 
            "/turtle1/pose", 
            self.pose_subscr_callback, 
            10
        )

        self.pose_publisher = self.create_publisher(
            Twist, 
            "/turtle1/cmd_vel", 
            10
        )

        self.get_logger().info("Turtle Controller is active.")


    def pose_subscr_callback(self, pose: Pose):
        self.get_logger().info(f"Current Pose: {pose}")

        twist = Twist()

        if(pose.x <= 2 or pose.x >= 9 or pose.y <= 2 or pose.y >= 9):

            twist.linear.x = 1.5
            twist.angular.z = 1 + random.random()

        else:
            twist.linear.x = 5.0

        self.pose_publisher.publish(twist)


def main(args = None):

    rclpy.init(args = args)

    node = Turtle_Controller()
    rclpy.spin(node)

    rclpy.shutdown()

