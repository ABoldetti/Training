#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>

typedef struct{
    char lab[3];
    int hi,hf;
    bool done;
} ora;

int main()
{
    char * c=NULL, *labo, *orainizio, *orafine;
    ora list[25];
    for ( int i=0 ; i<25 ; i++){
        while (((*c) = getchar()) != '\n');
        int len= sizeof(*c)/sizeof(char);
        int counter=0;
        for ( int i=0; i<len ; i++ ){
            if ( *(c+i) == " " ) counter ++;
            if ( counter == 0 ) *labo = *( c + i);
            if ( counter == 1 ) *orainizio = *( c + i);
            if ( counter == 2 ) *orafine = *( c + i);
            if ( counter >=3 ) {
                printf ( "sbagliato formato" );
                exit ( "EXIT_FAILED" );
            }
        }
        *(list+i) -> lab = *labo;
        *(list+i) -> hi = atoi (*orainizio);
        *(list+i) -> hf = atoi (*orafine);
    *c=NULL; 
    }
    return 0;
}
