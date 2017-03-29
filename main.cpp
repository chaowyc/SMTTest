#include <iostream>
#include "z3++.h"
#include <cstdio>
#include <dirent.h>
#include <sys/stat.h>
#include <string.h>
#include <vector>
#include <map>
#include <ctime>
#include <sys/time.h>
#include <fstream>
#include "FilePath.h"
#include "SmtSolver.h"
#include "StringInt.h"
#include<stdio.h>
#include<stdlib.h>
#include<stdarg.h>
#include<memory.h>
#include<setjmp.h>
#include "z3.h"
#include "CaluTime.h"
#include "ctpl_stl.h"
#include "FilePath.h"

using namespace std;

//bool subdirectory_flag = false;

int solved_case_num = 0;

int main(int argc, char *argv[])
{
    bool flag = false;

    /*
     *     argv[1] smt input file/directory
     *     argv[2] smt output directory
     */

    if(argc == 3)
    {
        // has output directory
        flag = true;
    }
    ctpl::thread_pool pp(4);
    if(IsDir(argv[1]))
    {
        // is directory
        TraverseDir(argv[1]);
        DeleteCSV();
        if(flag)
        {
            for(int i = 0; i < all_SMT_case_num; i++)
            {
                SmtSolver ssolver(SMT_file_list[i], argv[2]);
                ssolver.CollectAttr(1, i);
            }

        }
        else
        {
            for (int i = 0; i < all_SMT_case_num; ++i)
            {
                SmtSolver ssolver(SMT_file_list[i]);
                ssolver.CollectAttr(1, i);
            }
        }
    }
    else
    {
        // is single file
        if(flag)
        {
            SmtSolver ssolver(argv[1], argv[2]);
            ssolver.CollectAttr(-1, -1);
        } else
        {
            SmtSolver ssolver(argv[1]);
            ssolver.CollectAttr(-1, -1);
        }
    }

    return 0;
    //return 0;
}
