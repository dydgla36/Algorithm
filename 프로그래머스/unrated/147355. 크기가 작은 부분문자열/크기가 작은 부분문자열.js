function solution(t, p) {
    let answer = [];
    for(var i=0;i<t.length-p.length+1;i++) {
      answer.push(t.substring(i, p.length+i));   
    }
    answer = answer.filter((x) => x <= p);
    return answer.length;
}