function solution(a, b) {
    let sa = a.toString();
    let sb = b.toString();
    let ab = parseInt(sa + sb);
    let ba = parseInt(sb + sa);
    let answer = ab >= ba ? ab : ba;
    return answer;
}