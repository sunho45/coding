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
		adjlist.get(x).add(y);
	adjlist.get(y).add(x);
	}
	



public void printGraphToAdjList() {   
        System.out.println(size);	
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
