#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

bool start_click = false;

int isFile(char* filename){
    int retval = -1;
    FILE* ptr = fopen(filename, "r");
    if (ptr == NULL){
        retval = 0;
    } else {
        retval = 1;
    }
    fclose(ptr);
    return retval;
}


char* readFile(char* filename){
    FILE* ptr = fopen(filename, "r");
    if (ptr == NULL){
        printf("Error opening file!\n");
        exit(1);
    }
    fseek(ptr, 0, SEEK_END);
    size_t ptrsize = ftell(ptr);
    fseek(ptr, 0, SEEK_SET);
    char buffer[ptrsize + 1];
    fread(buffer, 1, ptrsize, ptr);
    buffer[ptrsize] = '\0';
    fclose(ptr);
    return strdup(buffer);
}

void writeFile(char* filename, char* content){
    FILE* ptr = fopen(filename, "w");
    fwrite(content, sizeof(char), strlen(content), ptr);
    fclose(ptr);
}
