function solution(dartResult) {
    const splitted = dartResult.split( '' );
    const length = splitted.length;
    let [ a, b, c ] = [ 0, 0, 0 ];
    let index = 0;
    let order = 0;
    while ( index != splitted.length ) {
        const value = splitted[ index ];
        const former = Number( ( splitted[ index - 2 ] + splitted[ index - 1 ] ) );
        const parsed = ( former || parseInt( splitted[ index - 1 ] ) );
        index++;
        if ( [ 'S', 'D', 'T' ].some( val => val == value ) ) {
            const calculated = Math.pow( parsed, ( value == 'S' ) ? 1 : ( value == 'D' ) ? 2 : 3 );
            if ( order == 0 ) {
                a = calculated;
            }
            else if ( order == 1 ) {
                b = calculated;
            } 
            else if ( order == 2 ) {
                c = calculated;
            }
            order++;
        }

        else if ( value == '*' ) {
            if ( order == 1 ) {
                a = ( a * 2 );
            }
            
            else if ( order == 2 ) {
                b = ( b * 2 );
                a = ( a * 2 );
            }
            
            else if ( order == 3 ) {
                c = ( c * 2 );
                b = ( b * 2 );
            }
        }
        
        else if ( value == '#' ) {
            if ( order == 1 ) {
                a = ( a * -1 );
            }
            else if ( order == 2 ) {
                b = ( b * -1 );
            }
            else if ( order == 3 ) {
                c = ( c * -1 );
            }
        }
    }
    return ( a + b + c );
}