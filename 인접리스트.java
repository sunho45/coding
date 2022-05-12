import java.io.*;
import java.util.*;
import java.util.Stack;
import java.util.Arrays;
import java.util.StringTokenizer;

class graph{
	
	
private int size;
	
	private ArrayList<ArrayList<Integer>> adjlist=new ArrayList();	
	
	
	public graph(int size) {
		this.size=size;
	}
	
	public void  inital(
			) {
		


		
		
	for(int i=0;i<size+1;i++) {
	adjlist.add(new ArrayList<Integer>() );
		
		
		
	}
	
	
	
	
	
	
	
	
	}
	
	
public void put(int x,int y) {
	if(x==y) {
		adjlist.get(x).add(y);
	}
	else {
		adjlist.get(x).add(y);
	adjlist.get(y).add(x);
	
	}
	int[] arr=(int[]) new int[adjlist.get(x).size()];
	int []arrl=(int[]) new int[adjlist.get(y).size()];
	for(int i=0;i<(int) adjlist.get(x).size();i++) {
	arr[i]=adjlist.get(x).get(i);	
	}
	for(int i=0;i<(int) adjlist.get(y).size();i++) {
		arrl[i]=adjlist.get(y).get(i);	
		}
	Arrays.sort(arr);//정렬 딱대
	Arrays.sort(arrl);
	adjlist.get(x).clear();
	adjlist.get(y).clear();
	for(int i=0;i<arr.length;i++) {
		adjlist.get(x).add(arr[i]);	
		}

	for(int i=0;i<arrl.length;i++) {
		adjlist.get(y).add(arrl[i]);	
		}


}
	
	



public void printGraphToAdjList() {   
        
	for(int i=0;i<adjlist.size();i++) {
		if(adjlist.get(i).size()>0) {
			System.out.print(i+"연결 그래프:");
			
		}
for(int j=0;j<adjlist.get(i).size();j++) {
			
			System.out.print(adjlist.get(i).get(j));
			if(j==adjlist.get(i).size()-1){
				
				break;
			}
			System.out.print("->");
		}
		
System.out.println();
		
		
	}
	
	
	
	
	
}	
}

public class WordSort {

	
	
	
	
	public static void main(String[] args)throws IOException {
	graph graph =new graph(6);
	graph.inital();
	
	graph.put(0, 2);
	graph.put(0, 4);
	graph.put(0, 0);
	graph.printGraphToAdjList();
	
		
	}

}
