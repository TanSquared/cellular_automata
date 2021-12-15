#include<stdio.h>
#include<stdlib.h>
#include <windows.h>

int size;

int prev(int i)
{
    if(i == 0) return (size - 1);
    return (i - 1);
}

int next(int i)
{
    return ((i + 1) % size);
}

int main()
{
    printf("Enter the rule ");
    int rule;
    scanf("%d", &rule);
    if(rule > 255) rule = rule % 255;
    if(rule < 0) rule = abs(rule) % 255;
    int* rulearr = (int *)malloc(8 * sizeof(int));
    int i, j;
    for(i = 0; i < 8; i++)
    {
        rulearr[i] = rule % 2;
        rule = rule / 2;
        //printf("%d\t", rulearr[i]);
    }
    printf("Enter the desired size of array ");
    scanf("%d", &size);
    if(size < 1 || size > 100) return 0;
    int* arr1 = (int *)calloc(size, sizeof(int));
    int* arr2 = (int *)calloc(size, sizeof(int));
    //arr1[3] = 1;
    arr1[size/2] = 1;
    for(i = 0; i < 250; i++)
    {
        for(j = 0; j < size; j++)
        {
            int x = arr1[prev(j)] * 4 + arr1[j] * 2 + arr1[next(j)];
            if(x > 7 || x < 0)
            {
                printf("x out of range\n");
                return 0;
            }
            int y = rulearr[x];
            arr2[j] = y;
            if(y == 0) printf(" ");
            else printf("O");
        }
        printf("\n");
        Sleep(100);
        for(j = 0; j < size; j++)
            arr1[j] = arr2[j];
    }
    return 0;
}
