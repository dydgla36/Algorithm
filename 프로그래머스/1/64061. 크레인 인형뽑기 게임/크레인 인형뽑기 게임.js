function solution(board, moves) {
    let answer = 0;
    moves = moves.map((v) => v - 1);

    let basket = [];
      for (let i in moves) {
        for (let j in board) {
          if (board[j][moves[i]] !== 0) {
            if (basket[basket.length - 1] === board[j][moves[i]]) {
              basket.pop();
              answer += 2;
            } else {
              basket.push(board[j][moves[i]]);
            }
            board[j][moves[i]] = 0;
            break;
          }
        }
      }

      return answer;
}