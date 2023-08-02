//
//  main.c
//  Esame
//
//  Created by Andrea Boldetti on 06/06/23.
//

#include <stdio.h>
#include <stdbool.h>
#define N 5

typedef struct{
    unsigned int i[10], f[10];
}blocco;
blocco date[N];
FILE* data;

void input(void);
void init(void);
void swap(unsigned int a[10]);
bool minor_date(unsigned int a[10], unsigned int b[10]);
bool overlap (blocco a, blocco b);
void full_mat(bool mat[N][N], bool *a);
void minimo_intervallo(void);

int main(int argc, const char * argv[]) {
    bool a=true;
    init();
    for (int j=0; j<N; j++){
        swap(date[j].i);
        swap(date[j].f);
    }
    bool mat[N][N];
    full_mat(mat, &a);
    if (a){
        printf("diocane");
        minimo_intervallo();
    }
    else{
        printf("madonna puttana");
    }
}

void input(void){
    data=fopen("data.dat", "r");
}

void init(void){
    input();
    int tmp;
    for (int i=0; i<N; i++){
        int counter=0;
        bool s=false;
        while ((tmp=getc(data))!='\n'){
            if (tmp==32){
                s=true;
                counter=0;
            }
            if (s) date[i].f[counter]=tmp;
            else date[i].i[counter]=tmp;
            counter++;
        }
    }
}

void swap(unsigned int a[10]){
    int tmp[2];
    tmp[0]=a[0];
    tmp[1]=a[1];
    a[0]=a[3];
    a[1]=a[4];
    a[3]=tmp[0];
    a[4]=tmp[1];
}
//questo programma per determinare quale data sia la minore ritorna Vero quando la prima è minore della seconda
bool minor_date(unsigned int a[10], unsigned int b[10]){
    for (int i=0; i<5; i++){
        if (a[i]<b[i]) return true;
        if (a[i]>b[i]) return false;
    }
    return false;
}

bool overlap (blocco a, blocco b){
    blocco tmp;
    if (minor_date(b.i, a.i)){
        tmp=b;
        b=a;
        a=tmp;
    }
//    so che a è il minore e b il maggiore
    return minor_date(b.i, a.f);
}

void full_mat(bool mat[N][N], bool *a){
    for (int i=0; i<N; i++){
        for (int j=0; j<N; j++){
            *(*(mat+j)+i)=overlap(date[i],date[j]);
            if (!(*(*(mat+j)+i))) a=false;
        }
    }
}

void minimo_intervallo(void){
    int tmp[2]={0,0};
    for (int i=1; i<N; i++){
        if (minor_date(date[tmp[0]].i, date[i].i)) tmp[0]=i;
        if (minor_date(date[i].f, date[tmp[i]].f)) tmp[1]=i;
    }
    printf("l'intervallo minore che comprende entrambe è: ");
}
