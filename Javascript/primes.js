function check_prime(n){
    if ( n <=1) return false
    if ( !n%2 ) return true
    for ( let i = 2 ; i< parseInt(Math.sqrt(n)) ; i++){
         if ( !n%i ) return true
    }
    return false
}

console.log( check_prime(17897667))