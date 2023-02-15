#include <stdio.h>
#include <string.h>
#include <stdlib.h>

unsigned char flag_encrypted[] = {
    0xea,0xf2,0xf5,0xff,0xf4,0xf3,0xe2,0xc1,0x8e,0x88,0x88,0x89,0xd7,0xf8,0xf6,0xe3,0xe5,0xd7,0x8e,0xf4,0xc7
};

int main(int argc, char** argv) {
    if(argc != 2) {
        printf("Please provide a flag\nExample: ./flagChecker [flag]\n");
        return 1;
    }

    unsigned char* flag_buffer = calloc(sizeof(flag_encrypted) + 1, 1);
    for(int i = 0; i < sizeof(flag_encrypted); i++) {
        flag_buffer[i] = flag_encrypted[i] ^ 0xba;
    }

    if(!strcmp(flag_buffer, argv[1])) {
        printf("Correct flag!\n");
    } else {
        printf("bad flag\n");
    }
    
    return 0;
}