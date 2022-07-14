cmake_minimum_required(VERSION 3.0.0)
project(Server VERSION 0.1.0)

#include(FetchContent)
#FetchContent_Declare(
#  cpprest
  # Specify the commit you depend on and update it regularly.
#  URL https://github.com/microsoft/cpprestsdk/archive/refs/heads/master.zip
#)
# For Windows: Prevent overriding the parent project's compiler/linker settings
#set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
#FetchContent_MakeAvailable(cpprest)

#include(CTest)
#enable_testing()

set(FULL_PATH_TO_MYSQL_CONNECTOR_CPP_DIR your_path_to_mysql_connectorcpp)
add_executable(Server main.cpp)
target_link_libraries(Server mysqlcppconn8)
target_compile_features(Server PRIVATE cxx_range_for)  

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
