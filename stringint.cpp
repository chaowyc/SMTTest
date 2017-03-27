//
// Created by chaowyc on 17-3-22.
//

#include <cstring>
#include <fstream>
#include "stringint.h"
stringint::~stringint()
{

}

stringint::stringint()
{
    string_vector_num = 0;
    string_vector_kind = 0;
}

int stringint::insert_map(string str)
{
    if(have_string(str))
    {
        //there is already str key in map, and the value of str add 1
        string_map[str]++;
        string_vector_num++;
    }
    else
    {
        // there is no str key in map, and initialize value with 1
        string_map[str] = 1;
        string_vector_num++;
        string_vector_kind++;
    }
    return 0;
}

bool stringint::have_string(string str)
{
    if(string_map.find(str) == string_map.end())
    {
        //there is no str key in map
        return false;
    }
    else
    {
        return true;
    }
}

int stringint::get_all_string(string outputfilepath) {
    std::ofstream output(outputfilepath);

    output << "summary:" << endl;
    output << "numbers:" << string_vector_num << endl;
    map<string, int >::iterator it;
    for(it = string_map.begin(); it != string_map.end(); it++)
    {
        output << it->first << ": " << it->second <<endl;
    }
    output.close();
    return 0;
}

int stringint::get_kindnum()
{
    return string_vector_kind;
}

int stringint::get_sum() {
    return string_vector_num;
}

void stringint::init()
{
    string_vector_num = 0;
    string_vector_kind = 0;
    string_map.clear();
}




