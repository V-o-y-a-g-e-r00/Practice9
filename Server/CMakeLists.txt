cmake_minimum_required(VERSION 3.0.0)
project(Server VERSION 0.1.0)

find_package(cpprestsdk REQUIRED)

add_executable(Server main.cpp)
#target_link_libraries(Server mysqlcppconn8 cpprestsdk::cpprest)

target_link_libraries(Server pthread cpprestsdk::cpprest -lcrypto)

#target_compile_features(Server PRIVATE cxx_range_for)  

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
