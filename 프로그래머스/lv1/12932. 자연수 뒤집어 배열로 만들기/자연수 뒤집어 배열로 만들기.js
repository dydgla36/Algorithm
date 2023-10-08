function solution(n) {
    let answer = [];
    let string = n.toString().split('')
    
    for (let i = string.length-1; i >= 0; i--) {
        answer.push(Number(string[i]))
    }
    return answer;
}