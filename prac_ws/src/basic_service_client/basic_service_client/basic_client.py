import sys

import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
from custom_msg_srv.srv import AddThreeNums


class MinimalClientAsync(Node):

    def __init__(self):
        super().__init__('basic_client')
        self.cli = self.create_client(
            AddThreeNums,
            'add_three_nums'
        )

        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().warn('service not available, waiting again...')

        self.req = AddThreeNums.Request()

    def send_request(self, a, b, c):

        self.req.a = a
        self.req.b = b
        self.req.c = c

        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)

        return self.future.result()


def main():
    rclpy.init()

    minimal_client = MinimalClientAsync()
    response = minimal_client.send_request(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]))

    minimal_client.get_logger().info(f"Result: {response.sum}")

    minimal_client.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
