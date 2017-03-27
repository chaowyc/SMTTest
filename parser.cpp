//
// Created by chaowyc on 17-3-25.
//

#include "parser.h"
#include <fstream>
#include <streambuf>
parser::parser(std::string file_path) {
    this->file_path = file_path;
    readall();
}
void parser::readall()
{
    std::ifstream in_file(file_path);
    smt_string.assign((std::istreambuf_iterator<char>(in_file)), std::istreambuf_iterator<char>());
}

void parser::print_string() {
    std::cout << smt_string << std::endl;
}

parser::~parser() {

}