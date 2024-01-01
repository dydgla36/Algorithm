function solution(nums) {
    let answer = 0;
    let cnt = nums.length / 2;
    let arr = nums.filter((element, index) => {
        return nums.indexOf(element) === index;
    });
    if(arr.length >= cnt){
        answer = cnt;
    }
    else{
        answer = arr.length;
    }
    return answer;
}