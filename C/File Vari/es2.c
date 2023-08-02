#include<stdio.h>

int main()
{
    char parenthesis[6]={'(',')','[',']','{','}' };
    char * c="/0";
    int j=0;
    while ( (*(c+j) = getchar()) != EOF ){
        for(int i=0; i<6;i++){
            if( parenthesis[i]==*(c+j)) printf("%c", parenthesis[i]);
        }
        j++;
    }
    return 0;
}