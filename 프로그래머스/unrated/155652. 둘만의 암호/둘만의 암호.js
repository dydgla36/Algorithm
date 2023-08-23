function solution(s, skip, index) {
    let answer = '';
    let alpha = new Set('abcdefghijklmnopqrstuvwxyz');
    [...skip].forEach(val => alpha.delete(val));
    const code = [...alpha];
    for (const i in s) {
        answer += code[(code.indexOf(s[i]) + index) % code.length];
    }
    return answer;
}