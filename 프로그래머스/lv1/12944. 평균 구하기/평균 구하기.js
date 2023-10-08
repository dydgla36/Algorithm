function solution(arr) {
    let answer = 0;
    for (let a = 0; a < arr.length; a++) {
        answer += arr[a];
    }
    return answer / arr.length;
}