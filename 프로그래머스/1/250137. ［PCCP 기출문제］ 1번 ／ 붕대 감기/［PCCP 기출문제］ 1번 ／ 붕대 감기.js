function solution(bandage, health, attacks) {
    let answer = health;
    let sections = [];
    
    let start = 0;
    for (let attack of attacks){
        let hitTime = attack[0]
        let damage = attack[1]
        let buff = (hitTime - start) * bandage[1] + Math.floor((hitTime - start) / bandage[0]) * bandage[2];
        sections.push(buff)
        sections.push(damage * (-1))
        start = hitTime + 1;
    }
    for (let section of sections){
        if (answer + section < 1){
            answer = -1;
            break;
        }
        else if (answer + section > health){
            answer = health;
        }
        else {
            answer = answer + section;
        }
    }
    return answer;
}