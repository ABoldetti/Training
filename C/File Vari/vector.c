#include <stdio.h>

void input(int c, int a[c]){
    for(int i=0;i<c;i++){
        scanf("%d",&a[i]);
        for(int j=0;j<i;j++){
            if(a[j]>=a[i]) printf("coglione");
        }
    }
}

void sort(int N, int a[N], int M, int b[M],int c[N+M]){
    int k=0,j=0;
    for(int i=0; i<(N+M);){
        for(;j<N;j++){
            for(;k<M;k++){
                if(b[k]<=a[j]){
                    c[i]=b[k];
                    i++;
                }else{
                    c[i]=a[j];
                    i++;
                    break;
                }
            }
            if(k==M){
                c[i]=a[j];
                i++;
            }
        }
    }
}


int main(){
    int N=5;
    int M=4;
    int a[N],b[M],c[N+M];
    input(N,a);
    input(M,b);
    sort(N,a,M,b,c);
    for(int i=0; i<(N+M);i++){
        printf("%d \n", *(c+i));
    }
return 0;
}