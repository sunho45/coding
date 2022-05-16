import java.util.*;

public class WordSort {

	
	
	
	static int N,E;
	static int [][] graph;

static boolean[] visited;
static boolean[] visitedd;
static int sum=0;
	public static void dfs(int node) {
		visited[node]=true;
		System.out.print(node+" ");
		
		for(int i=1;i<=N;i++) {
			
			if(!visited[i]&&graph[node][i]==1) {
				dfs(i);
			}
			
		}
		
		
	}
	public static void bfs(int node) {
		visitedd[node]=true;
		Queue<Integer> qu=new LinkedList();
		qu.add(node);
		while(!qu.isEmpty()) {
			
			int current=qu.remove();
			System.out.print(current+" ");
			
			for(int i=1;i<=N;i++) {
			if(!visitedd[i]&&graph[current][i]==1) {
				visitedd[i]=true;
				qu.add(i);
				
				
			}
			}
			
			
		
		
		}
		
		
		
	}
	
	
	
	
	
	
	public static void main(String[] args) {
	
		
		
		
		
		Scanner sc=new Scanner(System.in);
		N=sc.nextInt(); //정점의 개수
		
		E=sc.nextInt();// 간선의 개수
		int init=sc.nextInt();
		visited= new boolean[N+1];
		visitedd= new boolean[N+1];
		graph= new int[N+1][N+1];
		for(int i=0;i<E;i++) {
			int u=sc.nextInt();//정점의 번호 입력 받음
			int v=sc.nextInt();
			
			graph[u][v]=graph[v][u]=1;//간선이 있다면 1
		}
dfs(init);
System.out.println();
	bfs(init);

}


}
