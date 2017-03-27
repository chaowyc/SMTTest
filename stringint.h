//
// Created by chaowyc on 17-3-22.
//

#ifndef EX_STRINGINT_H
#define EX_STRINGINT_H

#include <map>
#define MAXOPERANDNUM 10000000

using namespace std;
class stringint {
private:
    //char *string_vector[MAXOPERANDNUM];
    map<string, int> string_map;
    //int string_vector_index;
    int string_vector_num;
    int string_vector_kind;
    bool have_string(string str);

public:
    stringint();
    int get_sum();
    int get_kindnum();
    //int insert_vector(char* str);
    int insert_map(string str);
    int get_all_string(string outputfilepath);
    void init();
    ~stringint();
};


#endif //EX_STRINGINT_H
