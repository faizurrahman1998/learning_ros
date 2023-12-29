import rclpy
from rclpy.node import Node

from example_interfaces.srv import AddTwoInts
from custom_msg_srv.srv import AddThreeNums

class MinimalService(Node):

    def __init__(self):
        super().__init__('basic_server')

        self.server = self.create_service(
            AddThreeNums, 
            'add_three_nums', 
            self.server_callback
        )

    def server_callback(self, request, response):

        response.sum = request.a + request.b + request.c
        self.get_logger().info('Incoming request\na: %d b: %d c: %d' % (request.a, request.b, request.c))

        return response


def main():
    rclpy.init()

    minimal_service = MinimalService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
