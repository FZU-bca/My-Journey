package lecture8;

public class Longdouble2strings {
	   public static void main(String[] args) {
		      long l = 14861584l;
		      String s1 = String.valueOf(l);
		      System.out.println(s1);
		      
		      double d = 24.5;
		      String s2 = String.valueOf(d);
		      System.out.println(s2);
		      
		      char ch = 'U';
		      String s3 = ch +"";
		      String s4 = Character.toString(ch);
		      System.out.println(s3);
		      System.out.println(s4);
		   }

}
