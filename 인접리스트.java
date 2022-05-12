import java.io.*;







import java.util.*;
import java.util.Stack;
import java.util.Arrays;
import java.util.StringTokenizer;

class graph{
	
	
int size;
	
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
	}
	
	



public void printGraphToAdjList() {   
        
	for(int i=0;i<adjlist.size();i++) {
		if(adjlist.get(i).size()>0) {
			System.out.print(i+"연결 그래프:");
			
		}
for(int j=0;j<adjlist.get(i).size();j++) {
			
			System.out.print(adjlist.get(i).get(j));
			
		}
		
System.out.println();
		
		
	}
	
	
	
	
	
}	
}

public class WordSort {

	
	
	
	
	public static void main(String[] args)throws IOException {
	graph graph =new graph(6);
	graph.inital();
	
	graph.put(0, 0);
	graph.printGraphToAdjList();
	
		
	}

}
	
	
