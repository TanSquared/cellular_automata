#include<stdio.h>
#include<stdlib.h>
#include<windows.h>
#include <stdlib.h>

int neighbour(int** lifearr, int xindex, int yindex, int sizex, int sizey)
{
    int ans = 0;
    int valuex, valuey;
    for(int i = -1; i < 2; i++)
    {
        for(int j = -1; j < 2; j++)
        {
            if(i == 0 && j == 0) ans = ans;
            else{
            valuex = xindex + i;
            valuey = yindex + j;
            if(valuex > -1 && valuey > -1 && valuex < sizex && valuey < sizey && lifearr[valuex][valuey] == 1)
                ans++;
            }
        }
    }
    return ans;
}

int main()
{
    int lsize, bsize;
    printf("Enter the number of rows you want ");
    scanf("%d", &bsize);
    printf("Enter the number of columns you want ");
    scanf("%d", &lsize);
    int** life1 = (int**)malloc(bsize * sizeof(int*));
    int** life2 = (int**)malloc(bsize * sizeof(int*));
    int i, j, k, val;
    for(i = 0; i < bsize; i++)
    {
        life1[i] = (int*)calloc(lsize , sizeof(int));
        life2[i] = (int*)calloc(lsize , sizeof(int));
        for(j = 0; j < lsize; j++)
        {
            life1[i][j] = rand() % 2;
            printf("%d ", life1[i][j]);
        }
        printf("\n");



    }

    int** temp = NULL;
    for(k = 0; k < 100; k++)
    {
        /*for(i = 0; i < bsize; i++)
        {
            for(j = 0; j < lsize; j++)
            {
                val = neighbour(life1, i, j, bsize, lsize);
                printf("%d", val);
            }
            printf("\n");
        }*/

        for(i = 0; i < bsize; i++)
        {
            for(j = 0; j < lsize; j++)
            {
                val = neighbour(life1, i, j, bsize, lsize);
                if(life1[i][j] == 1 && val < 2) life2[i][j] = 0;
                else if(life1[i][j] == 1 && val > 3) life2[i][j] = 0;
                else if(life1[i][j] == 0 && val == 3) life2[i][j] = 1;
                else life2[i][j] = life1[i][j];
                if(life2[i][j] == 1) printf("*");
                else printf(" ");
            }
            printf("\n");
        }
        //Sleep(1);
        system("cls");
        temp = life2;
        life2 = life1;
        life1 = temp;
    }
    return 0;
}
