function solution(book_time) {
    const sortedBookTime = book_time.sort();
    const usedRoom = [];
    for(let time of sortedBookTime) {
        const [[sH, sM], [eH, eM]] = time.map(x => x.split(":"));
        const startMin = Number(sH) * 60 + Number(sM);
        const endMin = Number(eH) * 60 + Number(eM) + 10;
        const idx = usedRoom.findIndex(x => x <= startMin);
        if(idx === -1) {
            usedRoom.push(endMin);
        } 
        else {
            usedRoom[idx] = endMin;
        }
    }
    return usedRoom.length;
}