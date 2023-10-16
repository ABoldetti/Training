/* idea di base del codice:
        nella congettura di collaz i numeri pari sono inutili da analizzare in quanto si rifanno ad un numero dispari.
        Quindi se si analizzano tutti i numeri dispari si stanno implicitamente analizzando anche tutti i numeri pari
*/

#include <stdio.h>

#define L 1

typedef unsigned long long ull;

int is_power_of_two( ull n){
    /*NON HO IDEA DI COME SI FACCIA HELP*/
    return 0;
}

int collaz( ull n){
        if (n%2){
            return(3*n + 1)/2;
        }
        else{
            while( n%2 && n>L){
                n/=2;
            }
            return n;
        }
}

int ciclo( ull var){
    ull num = var;
    int b= 1;
    if ( num > var || b ){  b = 0;
                            return ciclo(collaz(num));
    }
    else if ( num < var)    return 0;
    else                    return 1;
}

int main ( int argc, const char * argv[] ){
    int a;
    ull numero;
    printf(" Inserire un numero da usare come cap per la congettura di collaz \n");
    scanf("%lld" , &numero);
    if( !numero % 2 ) numero++;
    for ( ull i=2 ; i<numero ; i++ ){
        a = ciclo( i );
        if ( i ) printf("EUREKA %lld", i);
        else printf("Collassa a 0, %lld", i);
    }
}