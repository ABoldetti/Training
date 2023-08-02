#include <stdbool.h>
#include<math.h>
#include<stdio.h>

void arr(long digits, int n, int c[n]){
  for(int k=0; k<n;k++) c[k] = digits % (int)(pow (10 , k+1 ))/ pow (10 , k);
}

void manage( int n , int c[n]){
  for(int i = 0 ; i < n ; i++){
    if(i % 2)     c[i] *= 2;
    if(c[i]>9)    c[i] -= 9;
  }
}

bool validate(long digits) {
  int i;
  for(i = 0 ; pow ( 10 , i ) < digits ; i++);
  int c[i];
  long sum=0;
  arr( digits , i , c );
  manage( i , c );
  for(int j = 0 ; j < i ; j++){
    sum += c[j];
    }
  printf("%ld\n", sum);
  if(sum % 10 == 0) return true;
  else return false;
}

int main(){
    size_t a;
    bool b;
    scanf("%ld", &a);
    b=validate(a);
    if(b) printf("vero");
    else printf("falso");
return 0;
}