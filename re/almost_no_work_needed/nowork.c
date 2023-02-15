#include <stdio.h>
#include <string.h>
#include <wchar.h>

const wchar_t* flag = L"PHOENIX{N0_N33d_4_r3}";

int main(int argc, char** argv) {
    if(argc != 2) {
        printf("Please provide a flag\nExample: ./flagChecker [flag]\n");
        return 1;
    }
    if(strlen(argv[1]) > 100) {
        printf("Nice try :)\n");
        return 1;
    }

    wchar_t input_flag[100];
    swprintf(input_flag, 100, L"%hs", argv[1]);

    if(!wcsncmp(flag, input_flag, sizeof(input_flag))) {
        printf("Correct flag!\n");
    } else {
        printf("bad flag\n");
    }
    
    return 0;
}