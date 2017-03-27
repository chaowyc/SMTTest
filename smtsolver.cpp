//
// Created by chaowyc on 17-3-22.
//
#include <iostream>
#include "z3++.h"
#include <dirent.h>
#include <vector>
#include <map>
#include <ctime>
#include <sys/time.h>
#include <fstream>
#include "filepath.h"
#include "smtsolver.h"
#include <cstring>
#include "calutime.h"
#include "stringint.h"
#include <stack>
using namespace z3;

struct attributes smt_attr[MAXFILENUM];

//std::ofstream output_file("/home/chaowyc/z3Guide/file_out.csv");

stringint bitvector;
stringint operand;
stringint operation;
int smt_index = 0;
/*
 * visit the given smt3 expression recursively and count the operstions' number
 */
void visit(expr const & e)
{
    if (e.is_app())
    {
        unsigned num = e.num_args();
        if(num == 0)
            return;
        //std::cout << num << std::endl;
        for (unsigned i = 0; i < num; i++)
        {
            visit(e.arg(i));
        }
        // do something
        // Example: print the visited expression
        func_decl f = e.decl();

        std::string fname = f.name().str();
        int fkind = f.decl_kind();
        std::string exp = e.to_string();
        switch (fkind)
        {
            case 1024:
            {
                // bitvecoter
                bitvector.insert_map(exp);
                break;
            }
            case 2354:
            {
                // operand
                operand.insert_map(fname);
                break;
            }
            default:
            {
                // operation
                operation.insert_map(fname);
                break;
            }
        }
        //output_file << f.name() << ": " << f.decl_kind() << " " << e << "\n";
        //std::cout<<fname << ": " << fkind << endl;
        std::cout << '.';
    }
    else if (e.is_quantifier()) {
        visit(e.body());
        // do something
    }
    else {
        assert(e.is_var());
        // do something
        //func_decl f = e.decl();
        //std::cout << f.name() << std::endl;
    }
}

void visit2(expr const & e)
{
    std::stack<expr> sk;
    if(e.is_app())
    {
        unsigned num = e.num_args();
        for(int i = 0; i < num; i++)
        {
            sk.push(e.arg(i));
        }
        while(!sk.empty())
        {
        }
    }
}

void push_solver(char* smt_file_path)
{
    context ctx;
    //set_param("verbose", "999999");
    solver s(ctx);

    params p(ctx);
    p.set("timeout", (unsigned)90000);
    s.set(p);
    Z3_ast aa = NULL;
    try
    {
        aa = Z3_parse_smtlib2_file(ctx, smt_file_path, 0, 0, 0, 0, 0, 0);
    }
    catch (std::exception& e)
    {
        std::cout << e.what() << std::endl;
    }
    expr e(ctx, aa);
    s.push();
    s.add(e);
    calutime timer;
    timer.timer_begin();
    smt_attr[smt_index].push_smt_status = s.check();
    timer.timer_end();
    s.pop();
    smt_attr[smt_index].push_timespan = timer.time_span();
    printf("%s push solver spend time : %f\n", smt_file_path, timer.time_span());
    //timer.timer_begin();
    //visit(e);
    //timer.timer_end();
    //printf("visit spend time %f\n", timer.time_span());

}

void nopush_solver(char *smt_file_path)
{
    context ctx;
    //set_param("verbose", "999999");
    solver s(ctx);
    params p(ctx);
    p.set("timeout", (unsigned)90000);
    s.set(p);
    Z3_ast  aa = NULL;
    try
    {
        aa = Z3_parse_smtlib2_file(ctx, smt_file_path, 0, 0, 0, 0, 0, 0);
    }
    catch (std::exception& e)
    {
        std::cout << e.what() << std::endl;
    }
    expr e(ctx, aa);
    //s.push();
    s.add(e);
    //struct timeval t_start, t_end, t_result;
    //gettimeofday(&t_start, NULL);
    //int status = s.check();
    calutime timer;
    timer.timer_begin();
    smt_attr[smt_index].unpush_smt_status = s.check();
    timer.timer_end();
    smt_attr[smt_index].unpush_timespan = timer.time_span();
    printf("%s nopush solver spend time %f\n", smt_file_path, timer.time_span());

    timer.timer_begin();
    printf("begin visit\n");
    visit(e);
    timer.timer_end();
    printf("%s visit spend time %f\n", smt_file_path, timer.time_span());
}

void collect_attr(int id, char* file_path, int index)
{
    printf("thread: %d working\n", id);
    printf("%s\n", file_path);
    calutime timer;
    timer.timer_begin();
    bitvector.init();
    operand.init();
    operation.init();
    push_solver(file_path);
    nopush_solver(file_path);
    write_file(file_path);
    smt_index++;
    timer.timer_end();
    printf("thread:%d---------------------------spend time :%f---------------------------\n", id, timer.time_span());
    printf("%dth case completed\n", index);
    printf("finish%d/%d, %f processed..\n", smt_index, file_num, (1.0 * (smt_index + 1) / (file_num + 1)) * 100);
}
void test(char* file_path)
{
    /*
    bitvector.init();
    operand.init();
    operation.init();
    */
    push_solver(file_path);
    nopush_solver(file_path);
}
void write_file(char* file_path)
{
    char directory_path[PATHLENGTH] = {'\0'};
    get_output_path(file_path, directory_path);
    std::string timespan = directory_path;
    std::string bitvector_path = directory_path;
    std::string operand_path = directory_path;
    std::string operation_path = directory_path;

    timespan += "timespan.csv";
    bitvector_path += "bitvector.csv";
    operand_path += "operand.csv";
    operation_path += "operation.csv";

    ofstream timespan_file(timespan);
    timespan_file << "push_status\t" << "push_time\t" << "nopush_status\t" << "nopush_time\t" << endl;
    timespan_file << smt_attr[smt_index].push_smt_status << "\t" << smt_attr[smt_index].push_timespan << "\t" <<smt_attr[smt_index].unpush_smt_status << "\t" << smt_attr[smt_index].unpush_timespan << endl;
    bitvector.get_all_string(bitvector_path);
    operand.get_all_string(operand_path);
    operation.get_all_string(operation_path);
}

void test_pool(int id, const std::string & s)
{
    int i = 0;
    while(s[i++] != '\0')
        ;
    printf("%d\n", id);
}