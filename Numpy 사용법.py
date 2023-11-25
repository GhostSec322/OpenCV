## 다차원 배열을 효과적으로 처리 할 수 있도록 도와주는 도구 이다.
import numpy as np
x= np.array([1,2,3,4,5])
print("x:",x)
print(x.size)
print(x.dtype)
print(x[2])
##넘파이 데이터 초기화
#0부터 3까지의 배열 만들기
array1= np.arange(4)
print(array1)
## 0으로 초기화된배열 만들기
array2=np.zeros((4,4),dtype=int)
print(array2)
## 1로 초기화 된 배열 만들기
array3=np.ones((2,2),dtype=str)
print(array3)
# 0에서 9까지 랜덤하게 초기화 된 데이터 만들기
array4=np.random.randint(0,10,(3,3))
print(array4)

# 평균이 0이고 표준편차가 1인 표준정규를 띄는 배열 
array5= np.random.normal(0,1,(4,4))
print(array5)

## 배열 합치기
conarr1=np.random.randint(1,10,(4,4))
conarr2=np.random.randint(1,10,(4,4))
print(conarr1,"+",conarr2,"=",np.concatenate([conarr1,conarr2]))

##배열 형태 바꾸기
array_t=np.array([1,2,3,4])
print(array_t)
array2_t=array_t.reshape((2,2))
print(array2_t)
##세로축으로 합치기
arr_h=np.arange(4).reshape(1,4)
arr2_h=np.arange(8).reshape(2,4)
print(arr_h)
print(arr2_h)
array7=np.concatenate([arr_h,arr2_h],axis=0)
print(array7)
array8,array9=np.split([arr_h],[2],axis=1)
print(array8,array9)