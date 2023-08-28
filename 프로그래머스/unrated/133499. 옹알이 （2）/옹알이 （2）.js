function solution(babbling) {
    let possible = ["aya", "ye", "woo", "ma"];
    let nums = [...possible.keys()]
    let result = babbling.reduce((acc, cur) => {
        let prev = ''
        for (let idx = 0; idx < 4; idx++) {
            cur = cur.replaceAll(possible[idx], String(idx));
        }
        for (let ele of cur) {
            if (nums.includes(Number(ele)) && (prev != ele)) prev = ele
            else return acc
        }
        acc++
        return acc
    }, 0)
    return result
}