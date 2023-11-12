my_dict = {'0001101': 0, '0011001': 1,
           '0010011': 2, '0111101': 3,
           '0100011': 4, '0110001': 5,
           '0101111': 6, '0111011': 7,
           '0110111': 8, '0001011': 9}
c = int(input())
for tc in range(1, c + 1):
    n, m = map(int, input().split())
    data = [input() for _ in range(n)]

    code = []
    for row in reversed(data):  # 가장 아래쪽의 행부터 시작
        if '1' in row:
            idx = m - row[::-1].index('1') - 1  # 가장 오른쪽의 '1'의 위치
            while len(code) < 8 and idx >= 6:
                pattern = row[idx - 6:idx + 1]
                if pattern in my_dict:  # 패턴이 my_dict에 있으면
                    code.insert(0, my_dict[pattern])  # 암호코드를 리스트에 추가
                    idx -= 7  # 다음 패턴을 찾기 위해 인덱스를 7만큼 감소
                else:
                    idx -= 1  # 패턴이 아니라면 인덱스를 1만큼 감소
            if len(code) == 8:  # 암호코드가 8자리면 루프를 종료
                break

    # 암호코드의 유효성 검사
    check = (code[0] + code[2] + code[4] + code[6]) * 3 + code[1] + code[3] + code[5] + code[7]
    if check % 10 == 0:  # 암호코드가 유효하면
        result = sum(code)
    else:
        result = 0
    print(f'#{tc} {result}')  # 결과를 출력
