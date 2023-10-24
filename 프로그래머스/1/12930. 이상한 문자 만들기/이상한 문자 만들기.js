function solution(s) {
    let answer = s.split(" ");
    let result = [];
    for(let an of answer){
        for(let i=0; i<an.length; i++){
            if(i%2 === 0){
                result.push(an[i].toUpperCase());
            }else{
                result.push(an[i].toLowerCase());
            }
        }
        result.push(" ");
    }
    result.pop();
    return result.join("");
}