
def to_camel_case(text):
    a=text.split()
    for i in range (len(a)):

        if a[i] == "-" or a[i]== "_" :
            a[i]=' '
            a[i+1].upper()
            i = i - 1
    return ''.join(a)

print(to_camel_case("Tua_madre_succhia"))