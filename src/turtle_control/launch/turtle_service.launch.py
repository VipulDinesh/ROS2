from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
    Node(
        package='turtlesim',
        executable='turtlesim_node',
        output='screen'),
    ExecuteProcess(
        cmd=[[
            'ros2 service call ',
            '/kill ',
            'turtlesim/srv/Kill ',
            '"{name: turtle1}"'
        ]],
        shell=True
        ),
    ExecuteProcess(
        cmd=[[
            'ros2 service call ',
            '/spawn ',
            'turtlesim/srv/Spawn ',
            '"{x: 2, y: 2, theta: 0.2}"'
        ]],
        shell=True
        ),
    ])
