//
// Created by chaowyc on 17-3-25.
//

#ifndef EX_PARSER_H
#define EX_PARSER_H

#include <iostream>

class parser
{
private:
    std::string smt_string;
    std::string file_path;
    void readall();
public:
    parser(std::string file_path);
    ~parser();
    //test
    void print_string();
};


#endif //EX_PARSER_H
