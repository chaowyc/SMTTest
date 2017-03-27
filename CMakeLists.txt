cmake_minimum_required(VERSION 3.5)

project(EX)

set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES main.cpp filepath.h processpath.cpp smtsolver.h smtsolver.cpp stringint.cpp stringint.h calutime.cpp calutime.h threadpool.cpp threadpool.h parser.cpp parser.h)

find_package(Threads)
add_executable(EX ${SOURCE_FILES})
target_link_libraries( EX ${CMAKE_THREAD_LIBS_INIT} )

target_link_libraries(EX libz3.so)