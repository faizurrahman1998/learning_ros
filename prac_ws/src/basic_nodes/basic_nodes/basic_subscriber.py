import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Basic_Subscriber(Node):

    def __init__(self):
        super().__init__("basic_subscriber_node")
        self.subscriber = self.create_subscription(
            String, 
            "/chatter", 
            self.subscriber_callback, 
            10
        )

        self.get_logger().info("Basic Subscriber Node Created.")

    def subscriber_callback(self, msg: String):
        self.get_logger().info(f"Message: {msg.data}")


def main(args = None):

    rclpy.init(args = args)

    node = Basic_Subscriber()
    rclpy.spin(node)

    rclpy.shutdown()
