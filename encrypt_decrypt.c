#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int choice, key;
    char inputFile[260], outputFile[260];
    FILE *fin, *fout;
    int ch;

    printf("Press 1 to Encrypt file\n");
    printf("Press 2 to Decrypt file\n");
    printf("Enter your choice: ");
    scanf("%d", &choice);

    printf("Enter input file name: ");
    scanf("%s", inputFile);

    printf("Enter output file name: ");
    scanf("%s", outputFile);

    printf("Enter key: ");
    scanf("%d", &key);

    fin = fopen(inputFile, "rb");
    if (fin == NULL)
    {
        printf("Error: Input file not found!\n");
        return 1;
    }

    fout = fopen(outputFile, "wb");
    if (fout == NULL)
    {
        printf("Error: Cannot create output file!\n");
        fclose(fin);
        return 1;
    }

    if (choice == 1)
    {
        // Encryption
        while ((ch = fgetc(fin)) != EOF)
        {
            fputc(ch + key, fout);
        }
        printf("File encrypted successfully.\n");
    }
    else if (choice == 2)
    {
        // Decryption
        while ((ch = fgetc(fin)) != EOF)
        {
            fputc(ch - key, fout);
        }
        printf("File decrypted successfully.\n");
    }
    else
    {
        printf("Invalid choice!\n");
    }

    fclose(fin);
    fclose(fout);

    return 0;
}
