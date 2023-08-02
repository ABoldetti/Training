#include<stdio.h>
#include<stdbool.h>

#define N 3


typedef struct {
    int a,b,c;
} vec;

int f (vec a){
    return a.a*a.a+a.b*a.b-a.c*a.c;
}

void swap (vec data[N], int a, int b){
    vec ausy= data[b];
    for (int i=b; i>a ; i--){
        data[i]=data[i-1];
    }
    data[a]=ausy;
}

void sort (vec data[N]){
    int pivot=0;
    for (int i=1; i<N; i++){
        if ( f(data[pivot])>f(data[i])){
            swap(data, pivot, i);
            pivot=i;
        }
    }
}

void middle (vec data[N]){
    vec ausy;
    ausy.a= f(data[0]);
    ausy.b= f(data[N/2]);
    ausy.c= f(data[N-1]);
    if (ausy.a < ausy.b){
        if (ausy.a < ausy.c){
            if(ausy.b < ausy.c) swap (data, 0, N/2);
            else swap (data, 0, N-1);
        }
    }else{
        if (ausy.a > ausy.c){
            if (ausy.b<ausy.c) swap (data, 0, N/2);
            else swap (data, 0, N/2);
        }
    }

}


int main(int argc, char const *argv[])
{
    vec data[N];
    for (int i=0; i<N; i++){
        scanf("%d %d %d", &data[i].a, &data[i].b, &data[i].c);
    }
    middle (data);
    sort(data);
    printf("\n \n \n");
    for (int i=0; i<N; i++){
        printf("%d %d %d \n", data[i].a, data[i].b, data[i].c );
    }
    return 0;
}
