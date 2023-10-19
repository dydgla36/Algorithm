function solution(s) {
     let answer = "";
    s.split('').map(el => el.charCodeAt(0)).sort((a, b) => b - a).map(el => {answer += String.fromCharCode(el)});
    return answer
 
}