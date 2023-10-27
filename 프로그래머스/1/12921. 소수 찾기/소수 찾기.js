function solution(n) {
    let array = [];
    for(let i=2; i<=n; i++) {
        array[i] = i;
    }
    for(let i=2; i<=n; i++) {
        if(array[i]===0) continue;
        for(let j=i*2; j<=n; j+=i) {
            array[j] = 0;
        }
    }
    return array.filter(v => v!==0).length;
}