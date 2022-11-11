from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='my_package',
            executable='number_publisher',
            output='screen'),
        Node(
            package='my_package',
            executable='number_subscriber',
            output='screen'),
        Node(
            package='my_package',
            executable= 'pubsub',
            output='screen'),
    ])