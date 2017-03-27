//
// Created by chaowyc on 17-3-23.
//

#ifndef EX_CALUTIME_H
#define EX_CALUTIME_H

#include <ctime>
#include <sys/time.h>
class calutime {
private:
    struct timeval t_start, t_end, t_result;
    double result;
public:
    calutime();
    ~calutime();
    void timer_begin();
    void timer_end();
    double time_span();
};


#endif //EX_CALUTIME_H
