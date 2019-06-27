cmake_minimum_required (VERSION 3.9)
project (edl VERSION 0.9999 LANGUAGES C CXX)


find_package(VTK REQUIRED)

add_executable(edl edl.cxx)
target_link_libraries(edl ${VTK_LIBRARIES})
