import rclpy 
from rclpy.node import Node
from std_msgs.msg import String

class Basic_Publisher(Node):

    def __init__(self):

        self.__counter = 0

        super().__init__("basic_publisher_node")
        self.publisher = self.create_publisher(
            String, 
            "/chatter", 
            10
        )

        self.timer = self.create_timer(1.0, self.publisher_callback)
        self.get_logger().info("Basic Publisher Node Created.")
        


    def publisher_callback(self):

        msg = String()
        msg.data = f"{self.__counter}: Hello ROS World!"

        self.get_logger().info(f"Publishing: {msg}")
        self.publisher.publish(msg)

        self.__counter += 1.0


def main(args = None):

    rclpy.init(args = args)

    node = Basic_Publisher()
    rclpy.spin(node)

    rclpy.shutdown()
