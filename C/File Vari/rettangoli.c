#include<stdio.h>
#include<stdbool.h>
//0 vertice vicino all'origine, y1=y0, x0=x2, 
typedef struct {
    float x,y;
} point;

typedef struct{
    point v[4];
}rect;

void input (rect m){
    for(int i=0; i<4; i++){
        printf("inserire la coordinata X del %d° vertice\t", i+1);
        scanf("%f", &m.v[i].x);
        printf("inserire la coordinata Y del %d° vertice\t", i+1);
        scanf("%f", &m.v[i].y);
    }
    if(m.v[0].x!=m.v[2].x||m.v[1].x!=m.v[3].x||m.v[0].y!=m.v[1].y||m.v[3].y!=m.v[2].y) printf("THIS IS NOT A VALID RECTANGLE");
}
rect sovr(rect a, rect b){
    rect ausy;
    for(int i=0;i<4;i++){
        if(b.v[i].x>=a.v[0].x&& b.v[i].y>=a.v[0].y&&b.v[i].x<=a.v[3].x&& b.v[i].y<=a.v[3].y) ausy.v[i]=b.v[i];
        else ausy.v[i]=a.v[i];
    }
return ausy;
}

float area(rect a){
    float b;
    b=(a.v[3].x-a.v[0].x)*(a.v[3].y-a.v[0].y);
    return b;
}

int main(int argc, char const *argv[]){
    rect a,b,c;
    input (a);
    input (b);
    c=sovr(a,b);
    printf("area:\t %f\n", area(c));
    return 0;
}