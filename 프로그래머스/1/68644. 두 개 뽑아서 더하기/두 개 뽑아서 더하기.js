function solution(numbers) {
    let answer = [];

    for(let i=0; i<numbers.length; i++) {
        for(let j=i+1; j<numbers.length; j++) {
            let numSum = numbers[i]+numbers[j];
            if(!answer.includes(numSum)) answer.push(numSum);
        }
    }
    return answer.sort((a, b) => a-b);
}