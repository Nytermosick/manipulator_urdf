from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue
from launch.substitutions import Command
import xacro


def generate_launch_description():
    ld = LaunchDescription()
    
    use_sim_time = LaunchConfiguration('use_sim_time', default='false')

    package_path = FindPackageShare('manipulator_urdf')
    default_model_path = PathJoinSubstitution([package_path, 'models', 'manipulator.urdf'])
    robot_description_content = ParameterValue(Command(['xacro ', default_model_path]), value_type=str)
    
    default_rviz_config_path = PathJoinSubstitution([package_path, 'rviz', 'urdf.rviz'])
    
    ld.add_action(DeclareLaunchArgument(name='rviz_config', default_value=default_rviz_config_path,
                                        description='Absolute path to rviz config file'))
                                        
                                        
    robot_state_publisher = Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'use_sim_time': use_sim_time, 'robot_description': robot_description_content}])
    ld.add_action(robot_state_publisher)
    
    
 #   ld.add_action(Node(
 #       package='joint_state_publisher',
#        executable='joint_state_publisher'
#    ))
            
                                

    ld.add_action(Node(
        package='rviz2',
        executable='rviz2',
        output='screen',
        arguments=['-d', LaunchConfiguration('rviz_config')],
    ))

    return ld
