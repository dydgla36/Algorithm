function solution(n) {
    let num = (n+"").split('');
    num.sort(function(a, b) {
        return b-a;
    });
    let answer = Number(num.toString().replace(/\,/g,''));
    return answer;
}