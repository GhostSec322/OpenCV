#넘파이 상수연산
#1.더하기
import numpy as np
x=np.array([1,2])
print(x)
print(x+2)

arr=np.random.randint(1,20,size=4).reshape(2,2) ##1,20까지의 숫자 중 4개를 뽑아서 2by2형태로 저장
print(arr)
## 곱하기
print(arr*10)
## 서로 다른 형태의 배열 더하기
print(arr+x)
## 마스킹 연산
masking=np.random.randint(1,200,size=16).reshape(4,4)
print(masking <100)
##마스킹 연산 활용
ma=masking<100
masking[ma]=200
print(masking)
## 집계함수
fun_arr=np.arange(16).reshape(4,4)
print(np.mean(fun_arr))
print(np.sum(fun_arr))
print(np.max(fun_arr))
print(np.min(fun_arr))