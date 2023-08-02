#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
#include<string.h>

typedef struct{
    int indicatore, temperatura;
    bool a;
} misura;

#define N 5




int main(int argc, char const *argv[])
{
    misura * array = (misura *) malloc (sizeof(misura)*N);
    char * ind, * temp;
    bool t=false;
    char c;
    while ( c = getchar() != EOF ){
        if (c == 83) t=true;
        if (c == 84){
            t=false;
            *ind ="\0";
            *temp="\0";
        }
        if (t) temp=strcat(temp, c);
        if (!t) ind=strcat(ind, c);
        

        
    }
    return 0;
}
