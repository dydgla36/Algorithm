function solution(n, m) {
    let max;
    for(let i = 0; i <= n; i++) {
        if(n % i === 0 && m % i === 0) {
        max = i;
        }
    }
    let min = n * m / max;
    return [max, min];
}