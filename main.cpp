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
#include "filepath.h"
#include "smtsolver.h"
#include "stringint.h"
#include<stdio.h>
#include<stdlib.h>
#include<stdarg.h>
#include<memory.h>
#include<setjmp.h>
#include "z3.h"
#include "calutime.h"
#include "ctpl_stl.h"
#include "parser.h"

using namespace std;

void mmm(int id, const std::string & s, int ii) {
    std::cout << "mmm function " << id << ' ' << s << ii << '\n';
}

int main(int argc, char *argv[])
{
    //::testing::InitGoogleTest(&argc, argv);
    // argv[1] is the smt file/directory path

    ctpl::thread_pool p(4);
    for(int i = 0; i < argc; i++)
    {

        char* path = argv[i];
        printf("excute argv %d/%d\n", i, argc);
        for(int i = 0; i < file_num; i++)
        {
            file_list[i] = '\0';
        }
        traverse_file(path);
        for(int i = 0; i < file_num; i++)
        {
            //calutime timer;
            //timer.timer_begin();
            printf("%s\n", file_list[i]);
            p.push(collect_attr, file_list[i], i);
            //timer.timer_end();
            //printf("=======================argv %d spend time %f============================\n", i, timer.time_span());
        }
    }

    /*
     * rest
     */
    /*
    parser smt_parser("/home/chaowyc/z3Guide/QF_BV/brummayerbiere/367411/bitrev0032.smt2");
    smt_parser.print_string();
    */


    /*
    ctpl::thread_pool p(8);
    string s = "worked";
    p.push(mmm, s, 9);

    for(int i = 1; i < argc; i++)
    {
        file_num = 0;
        for(int i = 1; i < file_num; i++)
        {
            file_list[i] = {'\0'};
        }
        traverse_file(argv[i]);

        for(int i = 0; i < file_num; i++)
        {
            p.push(test_pool, file_list[i]);
        }
    }
     */

    return 0;
    //return 0;
}
