cmake_minimum_required(VERSION 3.5)

project(EX)

set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES C++/main.cpp C++/FilePath.h C++/FilePath.cpp C++/SmtSolver.h C++/SmtSolver.cpp C++/StringInt.cpp C++/StringInt.h C++/CaluTime.cpp C++/CaluTime.h C++/threadpool.cpp C++/threadpool.h)

find_package(Threads)
add_executable(EX ${SOURCE_FILES})
target_link_libraries( EX ${CMAKE_THREAD_LIBS_INIT} )

target_link_libraries(EX libz3.so)