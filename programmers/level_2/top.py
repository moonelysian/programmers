# 문제 설명
# 수평 직선에 탑 N대를 세웠습니다. 모든 탑의 꼭대기에는 신호를 송/수신하는 장치를 설치했습니다. 
# 발사한 신호는 신호를 보낸 탑보다 높은 탑에서만 수신합니다. 또한, 한 번 수신된 신호는 다른 탑으로 송신되지 않습니다.

# 예를 들어 높이가 6, 9, 5, 7, 4인 다섯 탑이 왼쪽으로 동시에 레이저 신호를 발사합니다. 
# 그러면, 탑은 다음과 같이 신호를 주고받습니다. 
# 높이가 4인 다섯 번째 탑에서 발사한 신호는 높이가 7인 네 번째 탑이 수신하고, 
# 높이가 7인 네 번째 탑의 신호는 높이가 9인 두 번째 탑이, 
# 높이가 5인 세 번째 탑의 신호도 높이가 9인 두 번째 탑이 수신합니다. 
# 높이가 9인 두 번째 탑과 높이가 6인 첫 번째 탑이 보낸 레이저 신호는 어떤 탑에서도 수신할 수 없습니다.
# 제한 사항
# heights는 길이 2 이상 100 이하인 정수 배열입니다.
# 모든 탑의 높이는 1 이상 100 이하입니다.
# 신호를 수신하는 탑이 없으면 0으로 표시합니다.

def solution(heights):
    answer = [0]*len(heights)
    while(heights):
        top = heights.pop()
        for i in range(len(heights)-1,-1,-1):
            if heights[i] > top:
                answer[len(heights)] = i+1
                break
    print(answer)
    return answer

solution([6,9,5,7,4])