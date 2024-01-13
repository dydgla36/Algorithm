function solution(n, k) {
    let answer = n * 12000
    answer += k * 2000
    answer -= parseInt(n / 10) * 2000
    return answer
}