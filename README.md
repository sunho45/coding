# 버블 정렬 정리

### 버블 정렬이란

파이썬의 정렬 알고리즘   
선택 정렬(Slection Sort)과 더불어 대표적인 O(N^2)의 시간복잡도를 가짐   
후반으로 갈수록 정렬 범위가 줄어 앞부분과 비교해 균일하게 같은 시간으로 정렬되지 않는다

### 버블 정렬의 작동 알고리즘
인접한 두 수를 비교해 조건에 맞춰 둘의 위치를 바꾼다.   
만약 밑 GIF처럼 오름차순으로 정렬한다면, 인접한 두 수를 비교해 왼쪽 수가 클 경우 왼쪽 수 기준 오른쪽 수와 자리를 바꾼다.   
왼쪽 수가 작을 경우 자리를 바꾸지 않고 옆으로 이동해 두 수를 비교한다.   

[버블 정렬 예시 GIF]   
![Bubble Sort](https://user-images.githubusercontent.com/77567577/168065176-533391a8-ea0c-4748-b97a-5d02777c7f71.gif)

### 버블 정렬 예시 코드
```python
def bubbleSort(arr):
    n = len(arr)
    
    for i in range(n):
        
        for j in range(0, n - i - 1):
           
            if arr[j] > arr[j + 1]: 
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = list(map(int, input().split()))

bubbleSort(arr)

print("[Sorted array is]")
for i in range(len(arr)):
    print("%d " %arr[i], end = "")
```

### 버블 정렬이 사용되는 예시
적은 케이스의 값들을 정렬할 때   
직관적인 정렬 방법을 확인하고 싶을 때

### 마치며
버블 정렬을 응용해 인접한 두 값이 정해진 차순과 다르게 배열되어 있다면,
바로 이전 값을 다시 검사하는 코드로 응용한다면 시간복잡도를 줄여 여러 곳에서 사용이 가능할 것 같다.

또한 for문을 하나 만들어 후반에 줄어드는 정렬 값을 체크해 시간복잡도를 줄일 수 있을 것 같다.

버블 정렬의 개선 버전으로 칵테일 정렬과 빗질 정렬이 있는데, 내가 생각한 방식과 어떤 점이 차이가 있는지 확인해도 좋을 것 같다.



![ezgif com-gif-maker (2)](https://user-images.githubusercontent.com/100903674/173194264-19d42cb6-12ad-4b58-9cd5-56d594932d01.gif)


