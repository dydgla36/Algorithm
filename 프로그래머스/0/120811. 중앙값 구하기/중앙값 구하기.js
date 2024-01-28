function solution(array) {
    let answer = 0
   let num = array.sort((a, b) => a-b)
   let A = Math.floor(num.length / 2)
   answer = num[A]
   return answer
}