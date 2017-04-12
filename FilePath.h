//
// Created by chaowyc on 17-3-22.
//

#ifndef EX_FILEPATH_H
#define EX_FILEPATH_H

#define MAXFILENUM 5000000
#define PATHLENGTH 256

extern char *SMT_file_list[MAXFILENUM];
extern char *CSV_file_list[MAXFILENUM];
extern bool has_result[MAXFILENUM];
extern int all_SMT_case_num;
extern int all_CSV_file_num;

char* StrContact(const char* str1, const char* str2);

int IsDir(char* path);

void TraverseDir(char* file_path);

void GetOutputPath(const char *file_path, char *output, char * smt_case_name);

bool IsTXT(const char *file_path);

bool IsCSV(const char *file_path);

//a function named DeleteCsv(), which is uesed to delete useless csv file
void DeleteCSV();
bool ContinueLastTime(char *path);
#endif //EX_FILEPATH_H
