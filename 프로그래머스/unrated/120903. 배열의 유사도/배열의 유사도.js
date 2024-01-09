function solution(s1, s2) {
    let list = s1.filter(x=>s2.includes(x));
    let answer = list.length;
    return answer;
}