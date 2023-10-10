function solution(n) {
    let answer = Math.sqrt(n);
    if(answer % 1 === 0 ) return (answer+1) * (answer+1)
    else return -1;
}
