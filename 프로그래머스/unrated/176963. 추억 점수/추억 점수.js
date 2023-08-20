function solution(name, yearning, photo) {
    var answer = [];
    
    const hash = new Map();
    
    name.forEach((val, i) => {
        hash.set(val, yearning[i]);
    });
    
    for (val of photo) {
        let sum = 0;
        for (ele of val) {
            const temp = hash.get(ele);
            if (temp) {
                sum += temp;
            }
        }
        answer.push(sum)
    }
    return answer;
}