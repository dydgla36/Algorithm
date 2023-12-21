function solution(n) {
    let answer = 0;
    let temp = n.toString(3);
    temp = temp.split("").reverse().join("");
    answer = parseInt(temp,3);
    return answer;
}