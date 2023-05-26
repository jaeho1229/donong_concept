'''
# 계산기 프로그램
# 조건문
# if 조건 :
# elif 조건 :
# else :

a=int(input("a를 입력하세요:"))# input()은 문자열을 입력받는다
b=int(input("b를 입력하세요:"))
op=input("연산자를 입력하세요:")
if op=='+':
    c=a+b
    print(f"a+b={c}")
elif op=='-':
    c=a-b
    print(f"a-b={c}")
elif op=='*':
    c=a*b
    print(f"a*b={c}")
elif op=='/':
    c=a/b
    print(f"a/b={c}")
else:
    print("연산자 오류")
'''

#음양수 판별 프로그램

a=int(input("a를 입력하세요:"))
if a>0:
    print("a=양수")
elif a<0:
    print("a=음수")
else:
    print("a=0")
