function solution(N, stages) {
    const People = stages.length;
    let step = new Array(N+2);
    stages.forEach(n => step[n] = (step[n] || 0)+1);
    let result = [];
    let num = People;
    let zero = [];
    for(let i=1; i<=N; i++) {
        if(!step[i]) {
            zero.push(i);
        } else {
            result.push([i, step[i]/num]);
            num -= step[i];
        }
    }
    result.sort((a, b) => {
        return b[1] - a[1];
    });
    return result.map(item => item[0]).concat(zero);
}