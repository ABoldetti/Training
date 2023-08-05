
def to_camel_case(text):
    #a=list(text)
    a = [i for a,i in enumerate(text) ]
    print(a)
    for i in range (0, len(text),1):
        print(i)
        print(a)
        if a[i] =="-" or a[i]=="_":
            a[i]=' '
            a[i].upper()
            i = i - 1
    return ''.join(a)

print(to_camel_case("Tua_madre_succhia"))