/*
 Andrea Boldetti 896999

 Prova di Laboratorio di informatica I del 06/06/2023

 Questo codice prende dallo standard input N intervalli di date e
 ritorna il grafo rappresentante le sovrapposizioni sottoforma di matrice di incidenza

 Nel caso in cui questi intervalli si sovrappongano
 tutti in un periodo,stampa quel periodo
*/


#include <stdio.h>
#include <stdbool.h>

#define N 20

//definisce il tipo di date e degli intervalli di date
typedef struct{
//		years, months, days
	int y,m,d;
} date;

typedef struct{
	date start,finish;
} intervals;

// definisce le variabili globali, tra cui l'array contenente tutti gli intervalli,
// e la matrice di incidenza
intervals es[N];
bool mat[N][N];



// dichiarazione di tutte le sottofunzioni usate
void input (void);
bool minor_date(date a, date b);
bool overlap(intervals a, intervals b);
void fill_mat(bool *a);
void printf_mat(void);
void minor_gap(void);



int main(int argc, const char * argv[]) {
 bool complete = true;
 input();
 fill_mat( &complete );
 printf_mat();
// complete diventa falso se nella matrice è presente almeno uno 0, sennò rimane vero
 if ( complete ){
  minor_gap();
 }else{
  printf( "Impossibile soddisfare tutte le esigenze\n" );
 }
return 0;
}



// funzione che riempe l'array di intervalli con tutte le varie date. Dato che il codice è fatto per
// ottenere intervalli di date interne al 2024, non immagazzina l'anno
void input ( void ){
	for( int i=0; i<N; i++ ) {
  scanf( "%d/%d/%d %d/%d/%d" , &es[i].start.d, &es[i].start.m, &es[i].start.y, &es[i].finish.d, &es[i].finish.m, &es[i].finish.y);
 }
}




// funzione che richiede in input due "date" e ritorna vero se "date a" è minore o uguale di "date b"
bool minor_date( date a, date b ){
//	conversione degli anni in mesi
	int deltay = a.y - b.y;
	a.m += deltay*12;
	
	if ( a.m<b.m ) return true;
	else	if( a.m>b.m ) return false;
			else 	if ( a.d<b.d ) return true;
					else 	if ( a.d>b.d ) return false;
							else return true;
}



// chiede in input due intervalli e ritorna vero se i 2 si intersecano, ritorna falso se le 2 sono separate
bool overlap( intervals a, intervals b ){
 intervals tmp;
 if ( minor_date(b.start, a.start) ){
  tmp = a;
  a = b;
  b = tmp;
 }
 return minor_date( b.start , a.finish );
}



// funzione che chiede in input un puntatore alla variabile booleana complete
//per riempire la matrice che controlla anche se è presente uno 0
void fill_mat ( bool *a ){
 for (int i=0; i<N; i++){
  for (int j=0; j<N; j++){
   *( *( mat + j ) + i ) = overlap( es[i] , es[j] );
   if (! *( *( mat + j ) + i )) *a = false;
  }
 }
}



// semplice funzione che stampa la matrice
void printf_mat(void){
 for (int i=0; i<N; i++){
  printf("|\t");
  for (int j=0; j<N; j++){
	  printf ("%d ", *(*(mat + j) + i));
  }
  printf("\t|\n");
 }
}



//funzione che scorre lungo tutto l'array di intervalli per vedere qual è la data d'inizio maggiore e la data di fine minore
void minor_gap(void){
 intervals gap;
 gap=es[0];
 for (int i=1; i<N; i++){
  if ( minor_date(es[i].finish, gap.finish) ) gap.finish=es[i].finish;
  if ( minor_date(gap.start, es[i].start)) gap.start=es[i].start;
 }
	printf("Il lasso di tempo in cui tutte le condizioni valgono è:\n");
	printf("%d/%d/%d \t %d/%d/%d\n", gap.start.d, gap.start.m, gap.start.y, gap.finish.d, gap.finish.m, gap.finish.y);
}
