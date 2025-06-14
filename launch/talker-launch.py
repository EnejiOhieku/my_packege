from launch import launch_description
from launch_ros.actions import Node

def generate_launch_description():
    return launch_description(
        [
            Node(
                package="demo_nodes_cpp",
                executable="Talker"
            )
        ]
    )