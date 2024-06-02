
# [디버그 문제]
# 직각삼각형 abc의 각 변의 관계는 a^2 + b^2 = C^2 과 같음
#
# 이 코드에서 1줄만 추가해서 코드를 수정할 것
# a = int(input())
# c = int(input())
#
# b_square = c - a
# print(b_square)

a = int(input())
c = int(input())

b_square = (c**2 - a**2)
print(b_square)

# pow 라는걸 처음 알았다.