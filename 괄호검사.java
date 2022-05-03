import java.util.*;



public class STACK {

	public static void main(String[] args) {
		Stack<Character> st=new Stack<Character>();
Scanner sc=new Scanner (System.in);
		
		String entered=sc.next();
		
		
		
		
		for(int i=0;i<entered.length();i++) {
			if(entered.charAt(i)=='{') {
				st.push('{');
				
				
			}
			if(entered.charAt(i)=='(') {
				st.push('(');
				
				
			}
			if(entered.charAt(i)=='[') {
				st.push('[');
				
				
			}
			if(entered.charAt(i)==')') {
				if(st.peek()=='(') {
					st.pop();
				}
				else {
				st.push(')');
				}
				
			}
			if(entered.charAt(i)=='}') {
				if(st.peek()=='{') {
					st.pop();
				}
				else {
				st.push('}');
				}
				
			}
			
			if(entered.charAt(i)==']') {
				if(st.peek()=='[') {
					st.pop();
				}
				else {
				st.push(']');
				}
				
			}
						
	}	
	if(st.isEmpty()) {
		System.out.print("참");
	}
		
	else {
		System.out.print("못지켰군요");
	}
		
		System.out.println(st.toString());		
}
\\well made by sinsunho
}
