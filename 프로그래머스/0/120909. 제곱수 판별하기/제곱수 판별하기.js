function solution(n) {
    let answer = (Math.sqrt(n) % 1 === 0) ? 1 : 2;
    return answer;
}