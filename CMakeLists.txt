cmake_minimum_required(VERSION 3.5)

project(EX)

set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES main.cpp FilePath.h FilePath.cpp SmtSolver.h SmtSolver.cpp StringInt.cpp StringInt.h CaluTime.cpp CaluTime.h threadpool.cpp threadpool.h)

find_package(Threads)
add_executable(EX ${SOURCE_FILES})
target_link_libraries( EX ${CMAKE_THREAD_LIBS_INIT} )

target_link_libraries(EX libz3.so)