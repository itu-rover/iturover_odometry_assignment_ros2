import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node


def generate_launch_description():
    pkg_share = get_package_share_directory('iturover_odometry_assignment')
    bag_path = os.path.join(pkg_share, 'rosbag', 'scenario')

    tf_publisher = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='tf_publisher',
        output='screen',
        arguments=[
            '--x', '0', '--y', '0', '--z', '0',
            '--yaw', '0', '--pitch', '0', '--roll', '0',
            '--frame-id', 'base_link',
            '--child-frame-id', 'odom',
        ],
    )

    bag_player = ExecuteProcess(
        cmd=['ros2', 'bag', 'play', bag_path, '--start-offset', '8', '--clock'],
        output='screen',
    )

    return LaunchDescription([
        tf_publisher,
        bag_player,
    ])
