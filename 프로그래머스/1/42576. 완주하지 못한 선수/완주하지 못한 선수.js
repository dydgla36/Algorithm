function solution(participant, completion) {
    const obj = {};
    const arr = [...participant, ...completion]
    for (let i = 0; i < arr.length; i++) {
        if (obj[arr[i]]) {
            delete obj[arr[i]] 
        } else {
            obj[arr[i]] = 1
        }
    }
    return Object.keys(obj)[0]
}