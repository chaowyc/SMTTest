//
// Created by chaowyc on 17-3-22.
//

#include <cstring>
#include <fstream>
#include "StringInt.h"


StringInt::StringInt()
{
    string_vector_num_ = 0;
    string_vector_kind_ = 0;
}

int StringInt::InsertMap(string str)
{
    if(HaveString(str))
    {
        //there is already str key in map, and the value of str add 1
        string_map_[str]++;
        string_vector_num_++;
    }
    else
    {
        // there is no str key in map, and initialize value with 1
        string_map_[str] = 1;
        string_vector_num_++;
        string_vector_kind_++;
    }
    return 0;
}

bool StringInt::HaveString(string str)
{
    if(string_map_.find(str) == string_map_.end())
    {
        //there is no str key in map
        return false;
    }
    else
    {
        return true;
    }
}

int StringInt::GetAllString(string outputfilepath) {
    std::ofstream output(outputfilepath);

    output << "summary:" << endl;
    output << "numbers:" << string_vector_num_ << endl;
    output << "kinds:" << string_vector_kind_ << endl;
    map<string, int >::iterator it;
    for(it = string_map_.begin(); it != string_map_.end(); it++)
    {
        output << it->first << ": " << it->second <<endl;
    }
    output.close();
    return 0;
}

int StringInt::GetKindnum()
{
    return string_vector_kind_;
}

int StringInt::GetSum() {
    return string_vector_num_;
}

void StringInt::Init()
{
    string_vector_num_ = 0;
    string_vector_kind_ = 0;
    string_map_.clear();
}

StringInt::~StringInt() {}
