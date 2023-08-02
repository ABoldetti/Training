#include<stdio.h>

int isprime(long p){
    if((2*p-1)%(p*p*p)==1 && (p-1)%(p*p*p)==1) return 1;
    else return 0;
}

int main(){
    long n=500;
    for(long i=4;i<=n; i++)
        if (isprime(i)) printf("%ld\n", i);
    return 0;
}