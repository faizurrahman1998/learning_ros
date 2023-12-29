import rclpy 
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class Turtle_Controller(Node):
    def __init__(self):
        super().__init__("Turtle_Controller_Node")
        self.turtle_controller = self.create_publisher(
            Twist, 
            "/turtle1/cmd_vel", 
            10
        )

        self.current_position = self.create_subscription(
            Pose, 
            "/turtle1/pose",
            self.got_message, 
            10
        )
        self.get_logger().info("Turtle Controller is Created.")


    def got_message(self, msg: Pose):
        self.get_logger().info(str(msg))

        cmd = Twist()

        if(msg.x >= 9):
            cmd.linear.x = 1.0
            cmd.angular.z = 0.8

        elif(msg.x <= 2):
            cmd.linear.x = 1.0
            cmd.angular.z = 0.8

        else:
            cmd.linear.x = 2.0

        self.turtle_controller.publish(cmd)

        

def main(args = None):

    rclpy.init(args=args)

    node = Turtle_Controller()
    rclpy.spin(node)

    rclpy.shutdown()
