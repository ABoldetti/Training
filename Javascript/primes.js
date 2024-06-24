function check_prime(n){
    if ( n <=1) return false
    if ( !(n%2) ) return false
    for ( let i = 2 ; i< parseInt(Math.sqrt(n)) ; i++){
         if ( !(n%i) ) return false
    }
    return true
}

console.log( check_prime(71))