
# 허프만 코드

## 허프만 코드의 각 함수에 대한 설명


새로운 노드를 만드는 함수이다. 새로운 노드의 구조체를 반환해준다.

```
node* makenode(char character, int freq, struct node* left, struct node* right)
{
	node* new_node = (node*)malloc(sizeof(node));
	new_node->character = character;
	new_node->freq = freq;
	new_node->left = left;
	new_node->right = right;
	return new_node;
}

```

### 주어진 값을 토대로 **허프만 트리**를 만들어야 한다.
``` 
node* make_Huffman_tree(char arr[])
```

```
{
	int i = 0;
	int j;
	int temp_n = 0;
	int min = 0;  //제일 빈도수가 작은 index
	int min2 = 0; //두 번째로 빈도수가 작은 index
	int fre[askii] = { 0 };  //문자(space~z) 빈도 수
	int check[askii] = { 0 };  //합쳐졌는지 확인(합쳐져서 살펴 볼 필요가 없으면 -1)
	node* tree[askii] = { NULL };  //비교할 노드 배열
	node* new_node; //새 노드


```

필요한 변수들을 선언해준다
```
	while (arr[i] != NULL)
	{
		//빈도수 구하기
		fre[arr[i]]++;
		i++;
	}
```	
예를 들어 공백(space)이 들어간다면 fre[31]의 값이 증가하고 arr[i] z라면 fre[121]의 값이 증가한다. 들어온 값이 AAZAZ라면 fre[64]의 값은 3고 fre[121]의 값은 2이다.








```	
	for (int i = 0; i < askii; i++)
	{
		//문자가 존재하면
		if (fre[i] != 0)
		{
			node_arr[ind] = *makenode(i, fre[i], NULL, NULL);//space부터 z까지
			tree[ind++] = makenode(i, fre[i], NULL, NULL); //노드 생성
		}
	}
```

공백(space)~z중에서 빈도수가 0이 아니라면 문자가 존재한다. 문자가 존재한다면 문자와 문자의 빈도수가 있는 노드를 생성한다.



```
	for (i = 0; i < ind - 1; i++)
	{
		//가장 작은 수 찾기
		j = 0;
		while (check[j] == -1)	j++; //합쳐진 노드를 제외한 배열 중 가장 앞 index
		min = j; //우선 제일 작다고 가정

		for (j = min; j < ind - 1; j++) //모든 배열을 검사
			if (check[j] != -1) //이미 합쳐진 노드가 아니면(검사해볼 필요가 있으면)
				if (tree[min]->freq > tree[j]->freq)
					//min인덱스 빈도수 보다 빈도수가 작은 경우
					min = j;

		//두번째로 작은 수 찾기
		j = 0;
		while (check[j] == -1 || j == min) j++;
		//합쳐진 노드와 최소 노드 제외한 배열 중 가장 앞 index
		min2 = j;  //두번째로 작다고 가정

		for (j = min2; j < ind; j++)
			if (check[j] != -1) //이미 합쳐진 노드가 아니면
				if (tree[min2]->freq > tree[j]->freq)
					//min2인덱스 빈도수 보다 빈도수가 작은 경우
					if (j != min) //가장 작은 index가 아닌 경우
						min2 = j;

```
가장작은 값과 가장큰 값의 배열 번호를 알아낸다. min은 가장 작은 원소의 인덱스 번호이고 min2는 두번째로 작은 원소의 인덱스 번호 값이다.


```
		tree[min] = makenode(NULL, tree[min]->freq + tree[min2]->freq, tree[min], tree[min2]);
		//min과 min2인덱스의 빈도수를 합친 빈도수로 새 노드 생성
		//새로 만든 노드를 min인덱스 자리에 넣는다.
```
가장작은수와 두번째로 작은수를 이어 두 빈도수의 합이 들어간 정보의 노드를 생성. 이러한 결합을  (문자열에 있는 알파벳의 개수-1)번한다.


```
		check[min2] = -1;
		//min2인덱스는 min인덱스 자리의 노드에 합쳐졌으므로 check[min2]<-=1
	}
	return tree[min]; //만들어진 트리의 루트 노드 반환
}

```
최종적으로 모든 값이 들어있는 트리의 루트노드를 반환시켜준다.



### 이제 허프만 테이블을 만들어 각 문자들을 encode 해준다

```
void make_table(node* n, char str[], int len, char* table[])
{
	if (n->left == NULL && n->right == NULL) //n이 단노드인 경우
	{
		str[len] = '\0'; //문장의 끝을 str끝에 넣어주고
						 //단 노드의 문자를 확인하여 table의 적절한 위치에 str문자열을 넣는다.
		strcpy(table[(n->character)], str);
	}
```	
노드의 자식이 없다면 노드의 문자를 확인하여 table의 적절하 위치에 str을 넣는다.

```
	else //단 노드가 아닌 경우
	{
		if (n->left != NULL) //왼쪽 자식이 있는 경우
		{
			str[len] = '0'; //문자열에 0 삽입
			make_table(n->left, str, len + 1, table);
			//재귀호출(문자열에 들어갈 위치에 +1)
		}
```
노드에게 왼쪽 자식이 있다면 0을 삽입

```
		if (n->right != NULL) //오른쪽 자식이 있는 경우
		{
			str[len] = '1'; //문자열에 1 삽입
			make_table(n->right, str, len + 1, table);
			//재귀호출(문자열에 들어갈 위치에 +1)
		}
		
		}
```		
노드에게 오른쪽 자식이 있다면 1을 삽입





```
int main()
{

	char arr[MAX]; //압축하고자 하는 문자열
	char* code[askii]; //각 문자에 대한 가변길이 코드 배열
	char str[MAX]; //문자열 변수
	char encoding[MAX] = ""; //인코딩해서 나온 이진수 배열
	int i; //반복문 변수
	char answer; //디코딩 원하는가에 대한 대답 변수
	node* root;//트리의 루트
	float num = 1.0;
	for (i = 32; i < askii; i++)
		code[i] = (char*)malloc(sizeof(char));

	printf("압축파일: ");
	scanf("%[^\n]s", arr); //압축하고자 하는 문자열 입력
	for (int i = 1; arr[i] != NULL; i++) {


		num++;
	}
	float num2 = 1.0;
	root = make_Huffman_tree(arr); //허프만코드를 이용한 트리 생성
	make_table(root, str, 0, code); //트리를 사용한 문자 별 가변길이 코드 생성

	i = 0;
	while (arr[i] != NULL) { //입력받은 문자열이 끝날때까지
		
		strcat(encoding, code[arr[i]]); //문자별 코드 인코딩 문자열 뒤에 넣기

		i++;
		
	}
	for (int o = 1; encoding[o] != NULL; o++) {

		num2++;

	}
	if (num == 1) {
		printf("압축결과 :   1 \n  ");
		printf("압축비 :   8 ");
	}


	else {
		for (i = 0; i < ind; i++)
			printf("%c : %s\n", node_arr[i].character, code[node_arr[i].character]);

		printf("압축 결과 : %s\n", encoding); //인코딩 한 이진수 배열 출력
		printf("압축비는 %f 이다\n", ((num * 8) / num2));
		printf("압축 해제 : ");
		decode(encoding, root);
	}

	return 0;
}


```
입력값을 받고 출력하는 
DEEE를 입력하고 다음과 같이 프로그램을 실행하면
![image](https://user-images.githubusercontent.com/100903674/162104486-d1640326-7cd4-430a-837b-c2fb3d7c7518.png)













다음과 같이 영어 대문자로 이루어진 문자열을 입력하면 인코딩된 이진 배열을 확인할 수 있다.
## 예외&정상적 
### 예외
예를들어 문자열 SSSSIIIIIINNNNNNNNTTTTTTTTTTTTEEEEEEEEEEEEEEE를 입력해보자
그러면 각 문자의 빈도수는 
S|I|N|T|E
---|---|---|---|---|
4|6|8|12|15


S|
---|
4

I|
---|
6

N|
---|
8

T|
---|
12


E|
---|
15

문자의 빈도수의 정보가 있는 노드들을 생성한다.

이러한 노드들을 트리 배열에 놓고 가장 작은 값과 두번쨰로 작은 값이 들어있는 노드들을 뽑아 서브트리를 만든다


이러한 과정들을 반복하면
![image](https://user-images.githubusercontent.com/100903674/162105641-91839cc3-cba9-474b-8b35-58ecbe73785a.png)

오른쪽 극단에서 뒤의 코드가 바뀌는 일이 있다. 하지만 디코딩의 prefix 성질은 만족하므로 큰 오류는 발생하지 않는다.

### 정상적
위와 같은 과정을 해본다면
![image](https://user-images.githubusercontent.com/100903674/162169112-feebdebf-956f-4d5a-b4c6-a33540897006.png)


A|B|C|D|E|F
---|---|---|---|---|---|
1010|1011|100|00|01|11

ABBCCDDDEEEEFFFFFF를 인코딩하면

10101011101110010000000001010101111111111111이 된다.


## 압축비
ex) 예를들어 문자열  ABBCCDDDEEEEFFFFFF을 압축해보자
아스키코드는 하나당 1바이트 즉 8비트를 할당한다. 반면 이진숫자 0,1은 하나당 1비트를 할당한다. 즉 압축비는
![image](https://user-images.githubusercontent.com/100903674/162105368-7fc970f3-ae01-473b-8d3f-e4c2b6f44f19.png)이다.









압축해보면

![image](https://user-images.githubusercontent.com/100903674/162158224-2ba9a3d3-0eb8-41ee-891f-ac11ffe00a65.png)



압축비는 3.2727이다.

이렇게 커다란 데이터덩어리를 최소한의 데이터 덩어리로 줄일 수 있다.


## 추가 예시
ex) 파일을 입력받는 코드를 추가해 이상한나라의 앨리스의 내용중 한 문장을 간략하게 가져와 허프만 코드화 해보았다.  
``` 
Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, "and what is the use of a book," thought Alice, "without pictures or conversations?"  
```
컴파일 결과는 아래와 같다.
![image](https://user-images.githubusercontent.com/101345032/162574659-3d6c4ba7-72df-4335-a14d-f831a1e092ec.PNG)

압축비는 1.919240이다.

이처럼 점점 데이터가 커지면 커질수록, 압축비 역시도 효율이 점점 줄어듬을 볼 수 있다.   
물론 압축을 해서 데이터상으로 이득을 볼 수 있을지 몰라도, 사용자의 번거러움까지 고려했을때 과연 압축하는 것이 이득이 될지 의문이 든다.
