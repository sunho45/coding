import java.util.*;



public class STACK {

	public static void main(String[] args) {
	
		
		Scanner sc = new Scanner(System.in);
		Stack<Integer> stack = new Stack<Integer>();
		
		int N = sc.nextInt();
		int[] arr = new int[N];
		
		for(int i = 0; i < N; i++) {
			arr[i] = sc.nextInt();
		}
 
 
		for(int i = 0; i < N; i++) {
			
			
			while(!stack.isEmpty() && arr[stack.peek()] < arr[i]) {
				arr[stack.pop()] = arr[i];
			}
			
			stack.push(i);
		}
		
			while(!stack.isEmpty()) {
			arr[stack.pop()] = -1;
		}
		
		
			StringBuilder sb = new StringBuilder();
			for(int i=0;i<N;i++)
				sb.append(arr[i]+" ");
			
			System.out.print(sb);

			
		
		
		
}

}
