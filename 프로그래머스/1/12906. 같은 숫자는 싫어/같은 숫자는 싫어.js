function solution(arr)
{
    let answer = arr;
    let result = [];
    for (let i=0; i<answer.length; i++){
        if(answer[i]!==answer[i+1]) result.push(arr[i]);
    }
    return result;
}