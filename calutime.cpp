//
// Created by chaowyc on 17-3-23.
//
#include <ctime>
#include <sys/time.h>
#include "calutime.h"

calutime::calutime()
{

}
calutime::~calutime()
{

}

void calutime::timer_begin()
{
    gettimeofday(&t_start, NULL);
}
void calutime::timer_end()
{
    gettimeofday(&t_end,NULL);
}

double calutime::time_span()
{
    timersub(&t_end, &t_start, &t_result);
    result = t_result.tv_sec + (1.0 * t_result.tv_usec) / 100000;
    return result;
}
