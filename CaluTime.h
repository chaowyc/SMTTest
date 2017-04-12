//
// Created by chaowyc on 17-3-23.
//

#ifndef EX_CaluTime_H
#define EX_CaluTime_H

#include <ctime>
#include <sys/time.h>
class CaluTime {
private:
    struct timeval t_start_, t_end_, t_result_;
    double result_;
public:
    CaluTime();
    ~CaluTime();
    void TimerBegin();
    void TimerEnd();
    double TimerSpan();
};


#endif //EX_CaluTime_H
