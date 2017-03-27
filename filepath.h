//
// Created by chaowyc on 17-3-22.
//

#ifndef EX_FILEPATH_H
#define EX_FILEPATH_H

#define MAXFILENUM 5000000
#define PATHLENGTH 300
extern char *file_list[MAXFILENUM];
extern int file_num;

char* str_contact(const char* str1, const char* str2);

int is_dir(char* path);

void traverse_file(char* file_path);

void get_output_path(char* file_path, char* output);

bool is_txt(char *file_path);

bool is_csv(char *file_path);
#endif //EX_FILEPATH_H
