function solution(s){
    let p = s.toLowerCase().split('p').length;
    let y = s.toLowerCase().split('y').length; 
    return p === y ? true : false;
}