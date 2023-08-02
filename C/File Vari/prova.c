#include <stdio.h>
#include <stdlib.h>

void read_attempt(char * str);
char * compare_attempt(char * str);


int main() {
    int counter = 0;
    char parola[5];
    printf("Inserisci la parola da indovinare:\n");
    for (int i = 0; i < 5; i++) {
        parola[i] = getchar();
    }
    
    while (counter < 6) {
        char attempt[5];
        printf("Tentativo numero %d:\n", ++counter);
        read_attempt(&attempt[0]);

    }
    
    
    return 0;
}
