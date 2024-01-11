function solution(num_list) {
    let answer = [0,0];
    for(let a of num_list){
        answer[a%2] += 1
    }
    return answer;
}