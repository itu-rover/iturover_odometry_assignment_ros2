cmake_minimum_required(VERSION 3.8)
project(iturover_odometry_assignment)

find_package(ament_cmake REQUIRED)

install(DIRECTORY
  launch
  rosbag
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
