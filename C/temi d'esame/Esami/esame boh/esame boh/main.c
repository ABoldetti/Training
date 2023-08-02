//
//  main.c
//  esame boh
//
//  Created by Andrea Boldetti on 03/07/23.
//

#define N 25
#define d 2

#include <stdio.h>
#include <stdlib.h>

typedef struct a{
    float x,y;
    struct a *next;
}type;

type *head;


void nuovonodo(float a, float b){
    type * newnode= malloc(sizeof(type));
    type * curs=head;
    newnode -> next = NULL;
    newnode -> x = a;
    newnode -> y = b;
    while (curs != NULL){
        curs=curs -> next;
    }
    curs=newnode;
}

float pendenza (type a, type b){
    return (b.y-a.y)/(b.x-a.x);
}

void removenode (type * a, type b){
    type * curs= head;
    while (curs->next!=a) curs=curs->next;
    type * newnode= malloc(sizeof(type));
    newnode->x=b.x;
    newnode->y=b.y;
    curs->next=newnode;
}

void sceglipilastro(type a){
    
    type * curs=head;
    type * ausy;
    while (curs != NULL){
        type * anticurs=curs->next;
        while (anticurs != NULL){
            if (pendenza(*curs, a)>pendenza(*curs, *anticurs)){
                removenode(anticurs, a);
                return;
            }
        }
        }
    nuovonodo(a.x, a.y);
    }




int main(int argc, const char * argv[]) {
    type ausy;
    ausy.x=0;
    printf("inserire l'altezza del primo pilastro");
    scanf("%f", &ausy.y);
    nuovonodo(ausy.x, ausy.y);
    ausy.x+=d;
    printf("inserire l'altezza del pilastro");
    scanf("%f", &ausy.y);
    nuovonodo(ausy.x, ausy.y);
    for (int i=2; i<N; i++){
        ausy.x+=d;
        printf("inserire l'altezza del pilastro");
        scanf("%f", &ausy.y);
        sceglipilastro(ausy);
        
        
    }
    return 0;
}
