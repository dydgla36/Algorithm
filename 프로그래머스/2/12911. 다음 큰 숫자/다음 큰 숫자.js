function solution(n) {
    let answer = 0;
    function findNum(num, next) {
        const two = next.toString(2).match(/1/g).length;
        if (num === two) answer = next;
        else findNum(num, next + 1);
    }
    const num = n.toString(2).match(/1/g).length;
    findNum(num, n + 1);
    return answer;
}