def main():
  print(solution("BBBBAAAABA"))
  
def solution(name):
  upDown = moveRight = moveLeft = countr = countl = 0
  
  for i, c in enumerate(name):
    upDown += min(ord(c) - ord('A'), ord('Z') - ord(c) + 1)
    
    # 오른쪽으로 이동하는 경우의 최소 이동 구하기
    # i = 0, 1, 2, ...
    if i != (len(name) - 1):      # 마지막 글자가 아닐 때
      if name[i + 1] == 'A':      # 다음 글자가 'A'이면
        countr += 1               # 건너뛰는 글자 수 카운트 1 증가
      else:                       # 다음 글자가 'A'가 아니면
        moveRight += countr + 1   # 건너뛴 만큼 더하고 해당 글자까지 한 번 더 이동
        countr = 0                # 카운트 초기화
    elif name[i] != 'A':          # 마지막 글자가 'A'가 아니면
      moveRight += countr         # 건너뛴 만큼 이동 횟수 추가
    
    # 왼쪽으로 이동하는 경우의 최소 이동 구하기
    # j = 0, -1, -2, ...
    j = -i
    if j != -(len(name) - 1):     # name[0]에서 시작하여 왼쪽으로 이동했으므로 name[-(len(name) - 1)]이 마지막 글자
      if name[j - 1] == 'A':
        countl += 1
      else:
        moveLeft += countl + 1
        countl = 0
    elif name[j] != 'A':
      moveLeft += countl
  
  return upDown + min(moveRight, moveLeft)

main()