cmake_minimum_required(VERSION 3.28)
project(Risk)

set(CMAKE_CXX_STANDARD 17)

find_package(Boost COMPONENTS math_c99 REQUIRED)
include_directories(${Boost_INCLUDE_DIR})

add_executable(Risk main.cpp)
target_link_libraries(${PROJECT_NAME} PRIVATE ${Boost_LIBRARIES})
