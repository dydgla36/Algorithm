function solution(a, b, n) {
    let answer = 0;
    let cola = 0;
    while(a<=n){
        let bottle = 0;
        if(n % a != 0){
            bottle = n - (a * Math.floor(n/a));
        }
        cola = Math.floor(n/a);
        answer += cola*b;
        n = cola * b + bottle;
    }
    return answer;
}