#include <stdio.h>

int main()
{

    int data[4];
    int hamming[7] = {0};

    printf("Enter the data bits\n");
    for (int i = 0; i < 4; i++)
    {
        scanf("%d", &data[i]);
    }

    hamming[2] = data[0];
    hamming[4] = data[1];
    hamming[5] = data[2];
    hamming[6] = data[3];

    hamming[0] = hamming[2] ^ hamming[4] ^ hamming[6];
    hamming[1] = hamming[2] ^ hamming[5] ^ hamming[6];
    hamming[3] = hamming[4] ^ hamming[5] ^ hamming[6];

    printf("This is the hamming code\n");

    for (int i = 0; i < 7; i++)
    {
        printf("%d", hamming[i]);
    }

    int hi;
    printf("Enter 1 for error or 0");
    scanf("%d", &hi);

    if (hi == 1)
    {
        int position;
        printf("Enter the position for error");
        scanf("%d", &position);
        position--;
        hamming[position] ^= 1;

        int p1 = hamming[0] ^ hamming[2] ^ hamming[4] ^ hamming[6];
        int p2 = hamming[1] ^ hamming[2] ^ hamming[5] ^ hamming[6];
        int p3 = hamming[3] ^ hamming[4] ^ hamming[5] ^ hamming[6];

        int final = (p1 * 1) + (p2 * 2) + (p3 * 4);
    }
    else
    {
        printf("no error");
    }

    return 0;
}