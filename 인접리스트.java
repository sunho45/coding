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
    for(int i=1; i<adjlist.size(); i++) {
        System.out.print("정점 " + i + "의 인접리스트");
        
        for(int j=0; j<adjlist.get(i).size(); j++) {
            System.out.print(" -> " + adjlist.get(i).get(j));
        }
        System.out.println();
    }
	
	
	
	
}
	
}

public class WordSort {

	
	
	
	
	public static void main(String[] args)throws IOException {
	graph graph =new graph(6);
	graph.put(1, 3);
	graph.put(1, 2);
	graph.printGraphToAdjList();
	
		
	}

}
