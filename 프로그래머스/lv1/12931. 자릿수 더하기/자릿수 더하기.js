function solution(n)
{
    let answer = 0;
    let arr = String(n).split("");
    arr.forEach((a)=>{
        answer += parseInt(a);
    });
    return answer;
}