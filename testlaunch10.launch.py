from launch import LaunchDescription
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.actions import Node

from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

import os
from ament_index_python import get_package_share_directory

def generate_launch_description():
    ld = LaunchDescription()

    
    
    
    robot_localization_node = Node(
       package='robot_localization',
       executable='ekf_node',
       name='test_ekf_localization_node_bag1_ekf',
       output='screen',
       parameters=[os.path.join( 'ekf4.yaml')],
       #remappings=[('odometry/filtered', 'odometry/global'),('geo_raw', 'imu/data')] #adding geo raw ->im data did nothing
       #parameters=[os.path.join( 'ekf2.yaml'),{'use_sim_time': LaunchConfiguration('use_sim_time')}]
)

    robot_map_node = Node(
       package='robot_localization',
       executable='ekf_node',
       name='ekf_filter_node_map', #this ones seems to have conectiones to geo raw at the minute
       output='screen',
       parameters=[os.path.join( 'ekf4.yaml')]
       #remappings=[('odometry/filtered', 'odometry/global'),('geo_raw', 'imu/data')] #adding geo raw ->im data did nothing
       #parameters=[os.path.join( 'ekf2.yaml'),{'use_sim_time': LaunchConfiguration('use_sim_time')}]
)

    navsat_node = Node(
           package='robot_localization',
           executable='navsat_transform_node',
           name='navsat_transform_node',
           output='screen',
           parameters=[os.path.join( 'ekf4.yaml')],
            #remappings = [
             #  ('geo_raw', 'imu/data'), #/geo_raw 'also the second option is the one that appears in the topic list
              # ('GPS','gps/fix'), #thing we want to rename first.....second is th enew name second is gps/fix
               #('gps/filtered', 'gps/filtered'),
               #('odometry/gps', 'odometry/gps'),
               #('odometry/filtered', 'odometry/filtered')
               #]
           
               
       #parameters=[os.path.join( 'ekf2.yaml'),{'use_sim_time': LaunchConfiguration('use_sim_time')}]
)
    
    
    

  
    ld.add_action(robot_localization_node)
    ld.add_action(robot_map_node)
    ld.add_action(navsat_node)
    
    #ld.add_action(robot_localization_node)
    

    return ld
