function solution(price, money, count) {
    let prices = 0;
    for(let i=1;i<=count;i++){
        prices += price * i;
    }
    return money > prices ? 0 : prices-money
}