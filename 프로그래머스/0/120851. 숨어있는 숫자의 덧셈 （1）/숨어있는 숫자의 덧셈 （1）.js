function solution(my_string) {
    let answer = 0;
    let num = /[^0-9]/g
    let cutStr = my_string.replace(num, "")
    let arrMy = Array.from(cutStr) 
    let mynum = arrMy.map(Number) 
    for(i = 0; i < mynum.length; i++) {
        answer += mynum[i]
    } 
    return answer


}