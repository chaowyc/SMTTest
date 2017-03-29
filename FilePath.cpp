//
// Created by chaowyc on 17-3-22.
//
#include <iostream>
#include "z3++.h"
#include <dirent.h>
#include <sys/stat.h>
#include <string.h>
#include <vector>
#include <map>
#include <ctime>
#include <fstream>
#include "FilePath.h"

char *SMT_file_list[MAXFILENUM];
char *CSV_file_list[MAXFILENUM];
int all_SMT_case_num = 0;
int all_CSV_file_num = 0;
// indicate whether the given directory has subdirectories, assume it hasn't subdirectories
//extern bool subdirectory_flag;

/*
 * connect the str1 and str2
 */

char* StrContact(const char* str1, const char* str2)
{
    char* result = NULL;
    result = (char*)malloc(strlen(str1) + strlen(str2) + 1);
    for(int i = 0; i < strlen(str1) + strlen(str2) + 1; i++)
    {
        result[i] = '\0';
    }
    //memset(result, sizeof(result), '\0');
    if(!result)
    {
        std::cout << "mallo memory failed" << std::endl;
        exit(1);
    }
    strcat(result, str1);
    strcat(result, str2);
    return result;
}

/*
 * return if path is a file or dirctory
 */

int IsDir(char* path)
{
    struct stat st;
    stat(path, &st);
    if(S_ISDIR(st.st_mode))
    {
        return 1;
    }
    else
    {
        return 0;
    }

}
/*
 * traverse the file and subdirctory on giving path
 */
void TraverseDir(char* file_path)
{
    //std::vector<std::string> file_list;
    file_path = StrContact(file_path, "/");
    DIR* dp;
    struct dirent* filename;
    dp = opendir(file_path);
    if(!dp)
    {
        std::cout << "open failed!" << std::endl;
        return;
    }
    while(filename = readdir(dp))
    {
        char* path = StrContact(file_path, filename->d_name);
        if(filename->d_name[0] == '.')
            continue;
        if(IsTXT(filename->d_name))
            continue;
        if(IsCSV(filename->d_name))
        {
            char *tmp = (char*)malloc(strlen(path) + 1);
            if(!tmp)
            {
                std::cout << "alloc memory for path failed" << std::endl;
                exit(1);
            }
            strcpy(tmp, path);
            CSV_file_list[all_CSV_file_num++] = tmp;
            continue;
        }
        //char* path = StrContact(file_path, filename->d_name);
        if(IsDir(path))
        {
            //std::cout << path << " dirctory" << std::endl;
            // the directory does has subdirectories
            /*
            if (!strcmp(filename->d_name, "smtoutput"))
            {
                continue;
            }
            else
            {
                subdirectory_flag = true;
                traverse_file(path);
            }*/
            TraverseDir(path);
        }
        else
        {
            char *tmp = (char*)malloc(strlen(path) + 1);
            if(!tmp)
            {
                std::cout << "alloc memory for path failed" << std::endl;
                exit(1);
            }
            strcpy(tmp, path);
            SMT_file_list[all_SMT_case_num++] = tmp;
            std::cout << path << std::endl;
        }
    }
    closedir(dp);
    return;
}



bool IsTXT(const char *file_path)
{
    int i = 0;
    while(file_path[i] != '\0')
        i++;
    if (file_path[--i] == 't'&& file_path[--i] == 'x' && file_path[--i] == 't')
    {
        return true;
    }
    else
    {
        return false;
    }

}

bool IsCSV(const char *file_path)
{
    int i = 0;
    while(file_path[i] != '\0')
        i++;
    if (file_path[--i] == 'v'&& file_path[--i] == 's' && file_path[--i] == 'c')
    {
        return true;
    }
    else
    {
        return false;
    }
}

void DeleteCSV()
{
    int status;
    for(int i = 0; i < all_CSV_file_num; i++)
    {
        status = remove(CSV_file_list[i]);
        if(status != 0)
        {
            std::cout << "delete error" << std::endl;
        }
    }
}


