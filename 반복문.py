'''
복습 문제#1
print(4!=4)
print(5>=10)
print(3==2)
'''

'''
#2번 과목 합불 프로그램
a=int(input("c언어 성적:"))
b=int(input("파이선 성적:"))
c=int(input("자바 성적:"))
sum=a+b+c
avg=sum/35
if avg>=80:
    print("합격")
else:
    print("불합격")
'''
'''
#3번
a=int(input("양의  정수를 입력 하세요"))
if  a%3==0 and a%2==0:
    print("2와 3의 배수")
elif a%3==0:
    print("3의 배수")
elif a%2==0:
    print("2의 배수")
else:
    print("이상한수")
'''
#4-1 숫자 맞추기 게임
import random
ans=random.randrange(0,10) # 0이상 10미만 숫자 랜덤 생성
c=0 #기회
while True:
    c=c+1
    print("---------------------")
    me = int(input("숫자입력"))
    if ans<me:
        print("down")
        print(f"기회 : {c}")
    elif ans>me:
        print("up")
        print(f"기회 : {c}")
    else:
        print("정답")
        print(f"기회 : {c}")
        break








        
# while 로 무한루프 만드는 법
while 0:
    num=input("알파벳을 입력 하세요(z를 누르면 종료):")
    if num=='z':
        break
    print(num)
