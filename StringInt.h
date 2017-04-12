//
// Created by chaowyc on 17-3-22.
//

#ifndef EX_STRINGINT_H
#define EX_STRINGINT_H

#include <map>
#define MAXOPERANDNUM 10000000

using namespace std;
class StringInt {
private:
    //char *string_vector[MAXOPERANDNUM];
    map<string, int> string_map_;
    //int string_vector_index;
    int string_vector_num_;
    int string_vector_kind_;
    bool HaveString(string str);

public:
    StringInt();
    int GetSum();
    int GetKindnum();
    //int insert_vector(char* str);
    int InsertMap(string str);
    int GetAllString(string outputfilepath);
    void Init();
    ~StringInt();
};


#endif //EX_STRINGINT_H
