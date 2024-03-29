#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include "inner_binary.h"

unsigned char key[] = {
    0x12, 0x34, 0xfa, 0xde
};

int main(int argc, char** argv) {
    printf("--Protected by bjarne secure protector--\n");

    // Decrypt the inner program
    unsigned char carry = 0b10101010;
    unsigned char* decrypted_buffer = malloc(inner_dll_encrypted_len);
    for(int i = 0; i < inner_dll_encrypted_len; i++) {
        unsigned char cipher_byte = inner_dll_encrypted[i] ^ key[i % 4] ^ carry;
        carry ^= key[i % 4];
        decrypted_buffer[i] = cipher_byte;
    }

    // Generate a random file name
    char tempPath[MAX_PATH];
    char tempName[MAX_PATH];
    GetTempPath(MAX_PATH, tempPath);
    GetTempFileName(tempPath, "temp", 0, tempName);

    HANDLE hFile = CreateFile(tempName, GENERIC_WRITE, 0, NULL, CREATE_ALWAYS, FILE_ATTRIBUTE_NORMAL, NULL);
    if (hFile == INVALID_HANDLE_VALUE)
    {
        sprintf("Failed to create file: 0x%lx\n", GetLastError());
        return 1;
    }

    // Write some data to the file
    DWORD bytesWritten = 0;
    if (!WriteFile(hFile, decrypted_buffer, inner_dll_encrypted_len, &bytesWritten, NULL))
    {
        printf("Failed to write to file: 0x%lx\n", GetLastError());
        CloseHandle(hFile);
        DeleteFile(tempName);
        return 1;
    }

    //Close the file handle
    CloseHandle(hFile);

    //Load the DLL and get handle to the internal file
    HANDLE hDll = LoadLibraryA(tempName);
    if(!hDll) {
        printf("Failed to load library: 0x%lx\n", GetLastError());
        return 1;
    }
    //Stop others from peeping by re-opening the file handle
    hFile = CreateFile(tempName, GENERIC_WRITE, 0, NULL, CREATE_ALWAYS, FILE_ATTRIBUTE_NORMAL, NULL);

    int (*inner_func)(int, char**) = GetProcAddress(hDll, "Run");
    if(!inner_func) {
        printf("Failed to get proc address: 0x%lx\n", GetLastError());
        return 1;
    }

    int ret_val = (*inner_func)(argc, argv);
    FreeLibrary(hDll);

    CloseHandle(hFile);
    DeleteFile(tempName);

    return ret_val;
}
