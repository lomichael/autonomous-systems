cmake_minimum_required(VERSION 3.10)
project(mujoco_controller)

set(CMAKE_CXX_STANDARD 11)

find_package(MuJoCo REQUIRED)

add_executable(mujoco_controller mujoco_controller.cpp)
target_include_directories(mujoco_controller PRIVATE ${MuJoCo_INCLUDE_DIRS})
target_link_libraries(mujoco_controller PRIVATE ${MuJoCo_LIBRARIES})
