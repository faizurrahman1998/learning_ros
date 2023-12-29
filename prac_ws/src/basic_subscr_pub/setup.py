from setuptools import find_packages, setup

package_name = 'basic_subscr_pub'

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
            "raw_publisher = basic_subscr_pub.raw_publisher:main", 
            "raw_subscriber = basic_subscr_pub.raw_subscriber:main", 
        ],
    },
)
