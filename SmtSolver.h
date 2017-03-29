//
// Created by chaowyc on 17-3-22.
//

#ifndef EX_SMT_H
#define EX_SMT_H

#include "StringInt.h"
#include "z3++.h"
using namespace z3;

class SmtSolver
{
private:
    int nopush_smt_status_;
    int push_smt_status_;
    double nopush_timespan_;
    double push_timespan_;
    std::string smt_file_path_;
    std::string output_path_;

    std::string timespan_output_path_;
    std::string bit_vector_output_path_;
    std::string operand_output_path_;
    std::string operation_output_path_;
    std::string case_name_;

    StringInt bit_vector_;
    StringInt operand_;
    StringInt operation_;

public:

    SmtSolver(std::string smt_file_path);

    SmtSolver(std::string smt_file_path, std::string output_path);

    ~SmtSolver();

    void GetOutputPath(const char* file_path, char* output, char* smt_case_name);

    void TraverseAST(int id, expr const & e);

    void PushSolver();

    void NoPushSolver(int id);

    void WriteFile();

    void CollectAttr(int id, int index);

    //void CollectAttr();
    /*
     * test method
     */
    void test(int id);
};

#endif //EX_SMT_H
