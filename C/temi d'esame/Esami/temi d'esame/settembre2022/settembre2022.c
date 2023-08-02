#include<stdio.h>
#include<stdlib.h>
#include<math.h>

#define pi 3.1415
#define g 9.80665
#define t 0.01

typedef struct nodo{
    float theta, v, a;
    struct nodo * next;
}node;

node * head = NULL;



node * inserimento (float a, float b, float c){
    node * ausy;
    ausy=(node *)malloc( sizeof(node) );
    if( ausy== NULL) exit( EXIT_FAILURE );
    ausy -> theta = a;
    ausy -> v = b;
    ausy -> a = c;
    ausy -> next = head;
    return ausy;
}

void firststep (float tm){
    float a,v,theta;
    a= -g * sin (tm);
    v= a*t;
    theta = tm + v*t;
    head=inserimento (theta,v,a);
}

void calc (){
    float a,v,theta;
    a= -g * sin (head->theta);
    v= head->v + a*t;
    theta = head->theta + v*t;
    head=inserimento (theta,v,a);
}

float conversione(float a){
    a *= pi / (float)(180);
    return a;
}

void loop (float tm){
    int counter=0;
    firststep( tm );
    while (counter<6){
        if (head -> theta >= tm) counter ++;
        calc();
    }
}

void stamp (){
    node * cur=head;
    while (cur -> next != NULL){
        printf ("%f\t%f\t%f\n", cur->theta, cur->v, cur->a);
        cur = cur -> next;
    }
}

void clr(){
    node * cur=head;
    long int ausy;
    while ( cur->next != NULL){
        ausy=cur->next;
        free(cur);
        cur=ausy;
    }
}

int main(int argc, char const *argv[])
{
    float tm;
    tm=atof(argv[1]);
    tm=conversione(tm);
    loop (tm);
    stamp ();
    clr();
    return 0;
}
