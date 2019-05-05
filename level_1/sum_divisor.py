# 문제 설명
# 자연수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.
# 제한 사항
#n은 0 이상 3000이하인 자연수입니다.

def solution(n):
    answer = sum([ i for i in range(1,n+1) if n%i==0 ])    
    return answer

# 다른 풀이
# def solution(n):
#     return n + sum([i for i in range(1, (n // 2) + 1) if n % i == 0])


