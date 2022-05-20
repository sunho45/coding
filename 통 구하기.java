import java.util.*;
import java.io.*;
public class Main
{
	public static void main(String[] args)throws IOException {
		Queue<Integer> qu=new LinkedList();
		Queue<Integer> qul=new LinkedList();
		LinkedList<Integer> LL=new LinkedList();
		
		StringBuilder sb=new StringBuilder();
		StringBuilder sbl=new StringBuilder();
		StringBuilder sbe=new StringBuilder();
		qu.add(7);
		qu.add(5);
		qu.add(6);
		qu.add(4);
		qu.add(2);
		qu.add(3);
		qu.add(7);
		qu.add(5);
		
		qul.add(7);
		qul.add(5);
		qul.add(6);
		qul.add(4);
		qul.add(2);
		qul.add(3);
		qul.add(7);
		qul.add(5);
		
		LL.add(7);
		LL.add(5);
		LL.add(6);
		LL.add(4);
		LL.add(2);
		LL.add(3);
		LL.add(7);
		LL.add(5);
	int	numy=LL.size();
		while(LL.size()!=0){
		   int capacity=10;
		   sbe.append("(");
		   for(int i=0;i<LL.size();i++){
		       
		   
		     if(capacity-LL.get(i)>=0){
		        
		         sbe.append(LL.get(i)).append(" ");
		         capacity-=LL.get(i);
		         LL.remove(i);
		         
		     }
		     
		     
		     
		       
		   } 
		   sbe.append(")");
		}
		
		
		
		
		
		float count=0;
		float num=qu.size();
		
		
		
		
		
		while(!qu.isEmpty()){
		    int capacity=10;
		    sb.append("(");
		    for(int i=0;i<=qu.size();i++){
		        if(capacity-qu.peek()>=0){
		            capacity-=qu.peek();
		            sb.append(qu.remove()+" ");
		            
		        }
		        else{
		            qu.add(qu.remove());
		        }
		        
		        
		        
		        
		        
		    }
		    sb.append(") ");
		    count++;
		    
		    
		    
		}
		 int capacity=10;
		 int countl=0;
		  int p=0;
		while(!qul.isEmpty()){
		    
		    
		    
		        capacity-=qul.peek();
		        if(capacity>=0){
		            while(p<1){
		                p++;
		                sbl.append("(");
		            }
		            
		            
		            sbl.append(qul.peek()+" ");
		            qul.remove();
		        }
		        
		    else{
		        sbl.append(")");
		           sbl.append(" ");
		        countl++;
		        p=0;
		       capacity=10; 
		    }
		    
		    
		    
		}
		sbl.append(")");
	System.out.println("최적해:"+sb);
	
		System.out.println("다음적합:"+sbl);
		
		System.out.println("최초적합:"+sbe);
		
		
		
		
		
	}
}
