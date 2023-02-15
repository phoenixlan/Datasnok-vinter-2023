#include <stdio.h>
#include <string.h>

const char* flag = "PHOENIX{S3cur3_drm_pr0t3ct10n}";

__declspec(dllexport) int Run(int argc, char** argv)
{
    if(argc != 2) {
        printf("Please provide a flag\nExample: secureFlagChecker.exe [flag]\n");
        return 0;
    }

    if(!strcmp(flag, argv[1])) {
        printf("Correct flag!\n");
        return 1;
    } else {
        printf("bad flag\n");
    }
    return 0;
}