function solution(n, arr1, arr2) {
    let answer = [];
    for (let i = 0; i < n; i++) {
        let tmp_1 = arr1[i].toString(2)
        let tmp_2 = arr2[i].toString(2)
        tmp_1 = '0'.repeat(n - tmp_1.length) + tmp_1
        tmp_2 = '0'.repeat(n - tmp_2.length) + tmp_2
        let final = ''
        for (let j = 0; j < n; j++) {
            if (tmp_1[j] == 1 || tmp_2[j] == 1) {
                final += '#'
            } else {
                final += ' '
            }
        }
        answer.push(final)
    }
    return answer;
}