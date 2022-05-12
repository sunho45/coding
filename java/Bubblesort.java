import java.io.BufferedReader;
import java.util.Arrays;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BubbleSort {

	public static void main(String[] args) throws IOException {
		BufferedReader br =new BufferedReader(new InputStreamReader(System.in));
		
		
	StringBuilder sb=new StringBuilder();
	System.out.println("원하는 숫자의 개수를 입력하시오");
			int N=Integer.parseInt(br.readLine());
			int []arr=new int[N];
			
	for(int i=0;i<N;i++) {
		int enter=Integer.parseInt(br.readLine());
		arr[i]=enter;
		
	}
	int temp;
	for(int i=0;i<N;i++) {
		
		
		for(int j=0;j<N-i-1;j++) {
			if(arr[j]>arr[j+1]) {
				temp=arr[j];
				arr[j]=arr[j+1];
				arr[j+1]=temp;
				
				
				
				
			}
			
			
		}
		
		
		
		
		
	}
	System.out.print('{');
	for(int i=0;i<N;i++) {
		sb.append(arr[i]);
		if(i==N-1) {
			break;
		}
		sb.append(',');
	}
	
	sb.append('}');
	System.out.println(sb);
	
	
}
	}
