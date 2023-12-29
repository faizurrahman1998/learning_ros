import rclpy 
from rclpy.node import Node
from turtlesim.msg import Pose

class Pose_Subsr(Node):

    def __init__(self):
        super().__init__("Pose_Subscriber_Node")
        self.pose_subs = self.create_subscription(
            Pose, 
            "/turtle1/pose", 
            self.subscr_callback, 
            10
        )

    def subscr_callback(self, msg: Pose):
        self.get_logger().info(str(msg))


def main(args = None):

    rclpy.init(args = args)

    node = Pose_Subsr()
    rclpy.spin(node)

    rclpy.shutdown()
