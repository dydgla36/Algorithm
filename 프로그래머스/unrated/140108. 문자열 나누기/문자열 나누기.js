function solution(s) {
    let answer=a=b=0;
    let word='';
    let isTrue = true;
    for(let i=0; i<s.length; i++){
        if(isTrue) word = s[i];
        if(word === s[i]) { 
            a++; 
            isTrue = false; 
        }
        else b++;
        if(a === b) {
            answer++;
            a=b=0;
            isTrue = true;
        }
    }
    return a === 0 && b === 0 ? answer : answer+1;
}