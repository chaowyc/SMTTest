//
// Created by chaowyc on 17-3-22.
//

#ifndef EX_SMT_H
#define EX_SMT_H

#include "stringint.h"
#include "z3++.h"
using namespace z3;

//extern std::ofstream output_file;

extern stringint bitvector;

extern stringint operand;

extern stringint operation;

struct attributes
{
    int unpush_smt_status;
    int push_smt_status;
    double unpush_timespan;
    double push_timespan;
    int var_num;
    //std::map<std::string, int > operation_map;
};

extern int smt_index;

extern struct attributes smt_attr[MAXFILENUM];

void visit(expr const & e);

void push_solver(char* smt_file_path);

void nopush_solver(char *smt_file_path);

void collect_attr(int id, char* file_path, int index);

void test(char* file_path);

void write_file(char* file_path);

void test_pool(int id, const std::string & s);

#endif //EX_SMT_H
