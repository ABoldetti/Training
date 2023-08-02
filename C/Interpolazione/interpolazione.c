#include <stdio.h> //fprintf(risultati," \n", );  fscanf(dati," ", );
#include <stdlib.h>
#include <math.h> // sqrt radice     pow potenza    nellla compilazione aggiungi -lm


int main(int argc, char *argv[])
{  int r = 0,c=4;
    // controllo comando d'esecuzione
    if ( argc < 2 )
    {
        printf ("Manca qualcosa nel comando d'esecuzione\n");
        exit (EXIT_FAILURE);
    }
    r = atoi (argv[1]);
    printf("numero di misure = %d\n",r);

// apertura e controllo del file
    FILE *dati;
    
    dati = fopen("input", "r");
    
    if ( dati == NULL ) 
    {
        printf("Errore\n");
        exit(EXIT_FAILURE);
    }
      
    double m[r][c];
    // lettura dei valori della matrice
    // considerala una matrice 3 X r dove nella prima colona ci sono i valori x nella seconda i valore y e nella terza le incertezze di y, ed in fine l'err x.
    // i dati vanno inseriti riga per riga, ovvero inserendo di seguito tutti i dati di una misura
    //Ipotizzando che i dati siano linerari calcola m e q con l'interpolazione!
    printf("inserisci valori della matrice\n");
    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c; j++)
        {
            fscanf(dati,"%lf", &m[i][j] );
        }
    }
    fclose(dati);

    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c; j++)
        {
            printf("%lf ", m[i][j]);
        }
        printf("\n");
    }

    double Sxx=0,Sx=0,Sy=0,Sxy=0,Ss=0,delta=0,b=0,a=0,errb=0,erra=0;
    // ricorda se vuoi lavorare sui valori di una colonna, metti il secondo indice fisso e fai scorrere la matrice

    for(int i=0; i<r; i++)
    {
        Sxx += (m[i][0]*m[i][0])/(m[i][2]*m[i][2]);
        }
    for(int i=0; i<r; i++)
    {
        Sx += m[i][0]/(m[i][2]*m[i][2]);
    }

    for(int i=0; i<r; i++)
    {
        Sy += m[i][1]/(m[i][2]*m[i][2]);
    }

    for(int i=0; i<r; i++)                    
    {
        Sxy += (m[i][0]*m[i][1])/(m[i][2]*m[i][2]);
    }

    for(int i=0; i<r; i++)
    {
        Ss += 1/(m[i][2]*m[i][2]);
    } 
    printf("Ss: %lf,Sx: %lf,Sxx: %lf,Sxy: %lf,Sy: %lf\n", Ss,Sx,Sxx,Sxy,Sy);

    delta = Ss*Sxx-(Sx*Sx);
    printf("delta vale %lf \n", delta);

    b = (Ss*Sxy-Sx*Sy)/delta;
    
    errb = sqrt(Ss/delta);
 
    a = (Sxx*Sy-Sx*Sxy)/delta;

    erra = sqrt(Sxx/delta);

    

    printf("i valori dell'interpolazione sono b=%lf a=%lf con errb=%lf erra=%lf  \n", b,a,errb,erra);

    // ora calcoliamo il coefficente corretto, tenendo conto dell'errore delle x

    for(int i=0; i<r; i++)
    {
        m[i][2]=sqrt((b*b*m[i][3]*m[i][3])+(m[i][2]*m[i][2]));
    }

    //stampa dei nuovi vaolori
    FILE *risultati;
    risultati = fopen("input", "w");
    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c; j++)
        {
            printf("%lf ", m[i][j]);
        }
        printf("\n");
        for (int j = 0; j < c-1; j++)
        {
             fprintf(risultati,"%lf ",m[i][j]);
        }
        fprintf(risultati,"\n");

    }
    fclose(risultati);

    // ricalcolo di a e b

    Ss=0;
    Sxx=0;
    Sx=0;
    Sxy=0;
    Sy=0;

    for(int i=0; i<r; i++)
    {
        Sxx += (m[i][0]*m[i][0])/(m[i][2]*m[i][2]);
    }

    for(int i=0; i<r; i++)
    {
        Sx += m[i][0]/(m[i][2]*m[i][2]);
    }

    for(int i=0; i<r; i++)
    {
        Sy += m[i][1]/(m[i][2]*m[i][2]);
    }

    for(int i=0; i<r; i++)
    {
        Sxy += (m[i][0]*m[i][1])/(m[i][2]*m[i][2]);
    }

    for(int i=0; i<r; i++)
    {
        Ss += 1/(m[i][2]*m[i][2]);
    }
    
    delta = Ss*Sxx-(Sx*Sx);
    printf("delta vale %lf \n", delta);

    b = (Ss*Sxy-Sx*Sy)/delta;
    
    errb = sqrt(Ss/delta);
 
    a = (Sxx*Sy-Sx*Sxy)/delta;

    erra = sqrt(Sxx/delta);

    printf("Ss: %lf,Sx: %lf,Sxx: %lf,Sxy: %lf,Sy: %lf\n", Ss,Sx,Sxx,Sxy,Sy);

    printf("i valori dell'interpolazione sono b=%lf a=%lf con errb=%lf erra=%lf  \n", b,a,errb,erra);

double X=0;
    if( a<=2*erra && a>=-2*erra)
    {
        double k,errk;
        k= Sxy/Sxx;
        errk= (1/sqrt(Sxx));
        printf("i valori dell'interpolazione sono k=%lf errk=%lf   \n", k,errk);

        // calcolo del chequadro sulla retta passante per l'origine 
        for (int i=0;i<r;i++)
        {
           X += ((m[i][1]-(k*m[i][0]))*(m[i][1]-(k*m[i][0])))/(m[i][2]*m[i][2]);
        }
    printf("il chi quadro della retta y=kx vale %lf \n", X);
    
    double Xr = X/(r-1);
    printf("il chi quadro ridotto vale %lf, con %d gradi di lib\n", Xr,r-1);
    }
else
{
    // calcola chiquadro di A+Bx
     for (int i=0;i<r;i++)
    {
        X += ((m[i][1]-a-(b*m[i][0]))*(m[i][1]-a-(b*m[i][0])))/(m[i][2]*m[i][2]);
    }
    printf("il chi quadro della retta y=A+Bx vale %lf \n", X);
    
    double Xr = X/(r-2);
    printf("il chi quadro ridotto vale %lf, con %d gradi di lib\n", Xr,r-2);
}


    exit(EXIT_SUCCESS);
}
