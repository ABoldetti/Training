strictmode = true

let a = []
let mosse = []

function create_table(){

    arr0 = [0,0,0]
    arr1 = [arr0,arr0,arr0]
    arr2 = [arr1,arr1,arr1]
    arr3 = [arr2,arr2,arr2]
    a = arr3
}

function print_table(){
    for ( let i=0 ; i<3 ; i++){
        a[i] = []
        for ( let ii=0 ; ii<3 ; ii++){
            a[i][ii] = []
            for ( let iii=0 ; iii<3 ; iii++){
                a[i][ii][iii] = []
                for ( let iv=0 ; iv<3 ; iv++){
                    console.log( a[i][ii][iii][iv])
                }
            }
        }
    }
}
create_table()
print_table()


while ( mosse.length < 81 || tris( a )){

}

function tris(){
    
}

function mossa(){
    if ( mosse.length%2 ) inserire_mossax()
    else inserire_mossay()
}