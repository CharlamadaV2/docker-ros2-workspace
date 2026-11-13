from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='uav_pck',
            node_namespace='',
            node_executable='',
            node_name='',

        )
    ])
