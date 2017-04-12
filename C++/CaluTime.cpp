//
// Created by chaowyc on 17-3-23.
//
#include <ctime>
#include <sys/time.h>
#include "CaluTime.h"

CaluTime::CaluTime()
{

}
void CaluTime::TimerBegin()
{
    gettimeofday(&t_start_, NULL);
}
void CaluTime::TimerEnd()
{
    gettimeofday(&t_end_,NULL);
}

double CaluTime::TimerSpan()
{
    timersub(&t_end_, &t_start_, &t_result_);
    result_ = t_result_.tv_sec + (1.0 * t_result_.tv_usec) / 100000;
    return result_;
}

CaluTime::~CaluTime()
{

}