import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class Draw_Circle(Node):

    def __init__(self):
        super().__init__("Draw_Circle_Node")
        self.cmd_vel_pub = self.create_publisher(Twist,"/turtle1/cmd_vel", 10)
        self.create_timer(2.0, self.send_velocity_command)
        self.get_logger().info("Draw Circle Node has started.")

    def send_velocity_command(self):
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 1.0
        self.cmd_vel_pub.publish(msg)

def main(args = None):

    rclpy.init(args = args)

    node = Draw_Circle()
    rclpy.spin(node)

    rclpy.shutdown()
