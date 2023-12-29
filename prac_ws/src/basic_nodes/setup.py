from setuptools import find_packages, setup

package_name = 'basic_nodes'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='fayez',
    maintainer_email='faizurrahman.fayez@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "basic_subscriber = basic_nodes.basic_subscriber:main",
            "basic_publisher = basic_nodes.basic_publisher:main",
            "turtle_controller = basic_nodes.turtle_controller:main",
        ],
    },
)
