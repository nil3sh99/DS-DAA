
public class NaiveSearch { 

	public static void search(String txt, String pat) 
	{ 
		int M = pat.length(); 
		int N = txt.length(); 

		for (int i = 1; i <= N - M; i++) { 

			int j; 

			for (j = 0; j < M; j++) 
				if (txt.charAt(i + j) != pat.charAt(j)) 
					break; 

			if (j == M) // if pat[0...M-1] = txt[i, i+1, ...i+M-1] 
				System.out.println("Pattern found at index " + i); 
		} 
	} 

	public static void main(String[] args) 
	{ 
		String txt = "AABAC"; 
		String pat = "AB"; 
		search(txt, pat); 
	} 
}

 
// Best case: When first string in pat is not present in the txt string
// Worst case: When all the strings in txt string are same

/* this code does not execute :-

public class NaiveSearch { 
	public static void search(String txt, String pat) 
	{ 
		int M = pat.length(); 
		int N = txt.length(); 
		int j=0;
		int i=0;
		while(i<N){
			if (txt.charAt(i) == pat.charAt(j)) {
				i++;
				j++;	 
			}
			if (j == M) // if pat[0...M-1] = txt[i, i+1, ...i+M-1] 
				System.out.println("Pattern found at index " + i); 
		} 
	} 

	public static void main(String[] args) 
	{ 
		String txt = "AABAC"; 
		String pat = "AB"; 
		search(txt, pat); 
	} 
}*/