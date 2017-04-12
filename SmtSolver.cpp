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
#include "FilePath.h"
#include "SmtSolver.h"
#include <cstring>
#include "CaluTime.h"
#include "StringInt.h"
#include <stack>

using namespace z3;

extern int solved_case_num;
extern int all_SMT_case_num;
extern std::vector<std::string> abort_smt_case;

void SmtSolver::test(int id)
{

    NoPushSolver(id);
    //write_file(file_path);
    WriteFile();
}
SmtSolver::SmtSolver(std::string smt_file_path)
{
    this->smt_file_path_ = smt_file_path;
    char tmp[PATHLENGTH] = { '\0' };
    char case_name[PATHLENGTH] = {'\0'};
    GetOutputPath(smt_file_path_.c_str(), tmp, case_name);
    this->output_path_ = std::string(tmp);
    this->case_name_ = std::string(case_name);
    this->timespan_output_path_ = output_path_ + case_name_ + ".ts.csv";
    this->bit_vector_output_path_ = output_path_ + case_name_ + ".bv.csv";
    this->operand_output_path_ = output_path_ + case_name_ + ".oa.csv";
    this->operation_output_path_ = output_path_ + case_name_ + ".op.csv";
}

SmtSolver::SmtSolver(std::string smt_file_path, std::string output_path)
{
    this->smt_file_path_ = smt_file_path;
    this->output_path_ = output_path + "/";
    char tmp[PATHLENGTH] = { '\0' };
    char case_name[PATHLENGTH] = {'\0'};
    GetOutputPath(smt_file_path.c_str(), tmp, case_name);
    //this->output_path_ = tmp;
    this->case_name_ = std::string(case_name);
    this->timespan_output_path_ = output_path_ + case_name_ + ".ts.csv";
    this->bit_vector_output_path_ = output_path_ + case_name_ + ".bv.csv";
    this->operand_output_path_ = output_path_ + case_name_ + ".oa.csv";
    this->operation_output_path_ = output_path_ + case_name_ + ".op.csv";
}

/*
 * visit the given smt3 expression recursively and count the operstions' number
 */
void SmtSolver::TraverseAST(int id, expr const &e)
{
    context ctx;
    //std::cout << e << endl;
    // unor
    std::map<std::string, int > unique_map;
    //std::unordered_map<std::string, int> unique_map;
    std::string str = Z3_ast_to_string(ctx, e);
    unique_map[str] = 1;
    //unique_map[str] = 1;
    std::stack<expr> sk;
    long int count = 1;
    if(e.is_app())
    {
        CaluTime timer;

        sk.push(e);
        timer.TimerBegin();
        while(!sk.empty())
        {

            expr e = sk.top();
            sk.pop();
            unsigned num = e.num_args();
            //std::cout << "nums: " << num << std::endl;
            for(int i = 0; i < num; i++)
            {
                if(e.is_app())
                {
                    std::string tmpstr = Z3_ast_to_string(ctx, e.arg(i));
                    if(unique_map.find(tmpstr) == unique_map.end())
                    {
                        // not in unqiue_map
                        sk.push(e.arg(i));
                        unique_map[tmpstr] = 1;

                    }
                    else
                    {
                        unique_map[tmpstr]++;
                        //std::cout << unique_map[tmpstr];
                    }

                }
            }

            func_decl f = e.decl();

            std::string fname = f.name().str();
            int fkind = f.decl_kind();
            //std::string exp = e.to_string();
            std::string exp = ToString(e);
            std::cout << fkind << std::endl;
            switch (fkind)
            {
                case 1024:
                {
                    // bitvecoter
                    bit_vector_.InsertMap(exp);
                    break;
                }
                case 2354:
                {
                    // operand
                    operand_.InsertMap(fname);
                    std::cout << fname << std::endl;
                    break;
                }
                default:
                {
                    // operation
                    operation_.InsertMap(fname);
                    break;
                }
            }

            if(count % 1000 == 0)
            {
                timer.TimerEnd();
                std::cout << "thread:" << id << " stack size:" << sk.size() << " time: " << timer.TimerSpan() << std::endl;
                if(timer.TimerSpan() > 100 || count >= 150000)
                {
                    std::cout << "calculate time is too long " << timer.TimerSpan() << std::endl;
                    abort_smt_case.push_back(smt_file_path_);
                    break;
                }
                timer.TimerBegin();
            }
            count++;
            //std::cout << "thread:" << id << " " << count << " stack size:" << sk.size() << std::endl;
            //std::cout <<fname << ": " << fkind << endl;
        }
    }
}

void SmtSolver::PushSolver()
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
        aa = Z3_parse_smtlib2_file(ctx, smt_file_path_.c_str(), 0, 0, 0, 0, 0, 0);
    }
    catch (std::exception& e)
    {
        std::cout << e.what() << std::endl;
    }
    expr e(ctx, aa);
    s.push();
    s.add(e);
    CaluTime timer;
    timer.TimerBegin();
    push_smt_status_ = s.check();
    timer.TimerEnd();
    s.pop();
    push_timespan_ = timer.TimerSpan();
    printf("%s push solver spend time : %f\n", smt_file_path_.c_str(), timer.TimerSpan());
}

void SmtSolver::NoPushSolver(int id)
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
        aa = Z3_parse_smtlib2_file(ctx, smt_file_path_.c_str(), 0, 0, 0, 0, 0, 0);
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
    CaluTime timer;
    timer.TimerBegin();
    nopush_smt_status_ = s.check();
    timer.TimerEnd();
    nopush_timespan_ = timer.TimerSpan();
    printf("%s nopush solver spend time %f\n", smt_file_path_.c_str(), timer.TimerSpan());

    timer.TimerBegin();
    printf("begin visit\n");
    TraverseAST(id, e);
    timer.TimerEnd();
    printf("%s visit spend time %f\n", smt_file_path_.c_str(), timer.TimerSpan());
}

void SmtSolver::CollectAttr(int id, int index)
{
    if(id != -1)
    {
        printf("thread: %d working\n", id);
    }
    else
    {
        printf("collect data...\n");
    }

    printf("%s\n", smt_file_path_.c_str());
    CaluTime timer;
    timer.TimerBegin();
    PushSolver();
    NoPushSolver(id);
    WriteFile();
    timer.TimerEnd();
    if(id != -1)
    {
        printf("thread:%d---------------------------spend time :%f---------------------------\n", id, timer.TimerSpan());
        printf("%dth case completed\n", index + 1);
        printf("finish %d/%d, %f processed..\n", ++solved_case_num, all_SMT_case_num, (1.0 * (solved_case_num) / (all_SMT_case_num + 1)) * 100);
    } else
    {
        printf("completed\n");
        printf("------------------------------------spend time :%f----------------------------\n", timer.TimerSpan());
    }

}

void SmtSolver::WriteFile()
{
    ofstream timespan_file(timespan_output_path_);
    timespan_file << "push_status\t" << "push_time\t" << "nopush_status\t" << "nopush_time\t" << endl;
    timespan_file << push_smt_status_ << "\t" << push_timespan_ << "\t" << nopush_smt_status_ << "\t" << nopush_timespan_ << endl;
    bit_vector_.GetAllString(bit_vector_output_path_);
    operand_.GetAllString(operand_output_path_);
    operation_.GetAllString(operation_output_path_);
}



SmtSolver::~SmtSolver() {}

template<typename T>
string SmtSolver::ToString(T val) {
    stringstream stream;
    stream << val;
    return stream.str();
}
