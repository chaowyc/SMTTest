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
#include "filepath.h"

char *file_list[MAXFILENUM];
int file_num = 0;

/*
 * connect the str1 and str2
 */

char* str_contact(const char* str1, const char* str2)
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

int is_dir(char* path)
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
void traverse_file(char* file_path)
{
    //std::vector<std::string> file_list;
    file_path = str_contact(file_path, "/");
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
        if(filename->d_name[0] == '.')
            continue;
        if(is_txt(filename->d_name))
            continue;
        if(is_csv(filename->d_name))
            continue;
        char* path = str_contact(file_path, filename->d_name);
        if(is_dir(path))
        {
            //std::cout << path << " dirctory" << std::endl;
            traverse_file(path);
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
            file_list[file_num++] = tmp;
            std::cout << path << std::endl;
        }
    }
    closedir(dp);
    return;
}

void get_output_path(char *file_path, char *output)
{
    int i = 0;
    int j = 0;
    // reach the tail of file_path
    while((file_path[i]) != '\0')
    {
        if(file_path[i] == '/')
        {
            j = i + 1;
        }
        i++;
    }
    int m = 0;
    while(m < j)
    {
        output[m] = file_path[m];
        m++;
    }
}

bool is_txt(char *file_path)
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

bool is_csv(char *file_path)
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

