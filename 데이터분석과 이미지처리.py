import numpy as np

arr=np.arange(0,10)
np.save('saved.npy',arr)
result =np.load('saved.npy')
print(result)

array1 =np.arange(0,10)
array2 =np.arange(10,20)
np.savez("saved2.npz",array1=array1,array2=array2)

data= np.load('saved2.npz')
print(data['array1'])
print(data['array2'])
##Numpy원소 정렬
##오름차순
array=np.arange(1,20)
array.sort()
print(array)
##내림차순
print(array[::-1])
#각 열을 기준으로 정렬 
x= np.array([[1,4,5,7,9],[8,3,4,2,5]])
print(x)
x.sort(axis=0)
print(x)

##균일간격 데이터 생성
x=np.linspace(0,10,5)
print(x)

##난수의 재연 (실행마다 결과 동일)
np.random.seed(7)
print(np.random.randint(0,10,(2,3)))

##넘파이 배열객체 복사
array1= np.arange(0,10)
array2=array1
array2[0]=99
print(array1)
##이 문제 해결
array4= np.arange(0,10)
array3=array4.copy()
array3[0]=99
print(array4)
##중복제거
arrrm=np.array([1,1,2,2,3,3,4,4,5,5])
print(np.unique(arrrm))