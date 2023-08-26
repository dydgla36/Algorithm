function solution(k, m, score) {
  let answer = 0;
  const sorted = score.sort((a, b) => b - a);   //오름차순
  sorted.forEach((key, idx) => {    //배열순회
    if (idx % m === 0  && score[idx + m - 1]) {
      answer += score[idx + m - 1] * m;
    }
  });

  return answer;
}