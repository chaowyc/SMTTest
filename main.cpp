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
std::vector<std::string> abort_smt_case;

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
    //ctpl::thread_pool pp(4);
    if(IsDir(argv[1]))
    {
        // is directory
        TraverseDir(argv[1]);
        //DeleteCSV();
        if(flag)
        {
            for(int i = 0; i < all_SMT_case_num; i++)
            {
                SmtSolver ssolver(SMT_file_list[i], argv[2]);
                ssolver.CollectAttr(1, i);
                //pp.push([&](int id){ssolver.CollectAttr(id, i);});
            }
        }
        else
        {
            for (int i = 0; i < all_SMT_case_num; ++i)
            {
                char tmp_path[PATHLENGTH] = {'\0'};
                char tmp_name[PATHLENGTH] = {'\0'};
                GetOutputPath(SMT_file_list[i], tmp_path, tmp_name);
                if(!ContinueLastTime(tmp_path))
                {
                    SmtSolver ssolver(SMT_file_list[i]);
                    ssolver.CollectAttr(1, i);
                } else
                {
                    printf("%s already has result!\n", SMT_file_list[i]);
                    continue;
                }
            }
        }
        printf("Abort SMT Case:");
        for(int i = 0; i < abort_smt_case.size(); i++)
        {
            printf("%s\n", abort_smt_case[i]);
        }
        printf("output to a file ? (y/n) \n");
        char ch;
        scanf("%c", &ch);
        switch (ch)
        {
            case 'y':
            {
                printf("file name: ");
                std::string output;
                std::cin >> output;
                ofstream out(output);
                for(int i = 0; i < abort_smt_case.size(); i++)
                {
                    out << abort_smt_case[i] << std::endl;
                }
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
