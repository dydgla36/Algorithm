function solution(want, number, discount) {
    let answer = 0;
    const isMatch = (discount) => {
        let map = new Map();
        discount.forEach((d) => map.set(d, (map.get(d) || 0) + 1));
        for (let i = 0; i < want.length; i++) {
            if (map.get(want[i]) !== number[i]){
                return false;
            };
        };
        return true;
    };

    for (let i = 0; i <= discount.length - 10; i++) {
        const sliceArr = discount.slice(i, i + 10);
        if (isMatch(sliceArr)){
            answer += 1;
        };
    };
    
    return answer;
}