numero=int(input('inserire un numero intero positivo '))
a=2
c=0
while a<=numero/2:
    b=numero%a
    if b==0:
        c=c+1 #variabile ausiliaria per controllare se esistono divisori
    a=a+1
if c>0:
    
    print(numero, 'non è un numero primo e ha: {}'.format(c), 'divisori')
else:
    print(numero, 'è un numero primo')
