public class similar
{
	public static void main(String args[])
	{
		String s1 = new String("Hello world"), s2 = new String("Hello World");
		int len1 = s1.length(), len2 = s2.length();
		if(len1 == len2)
		{
			System.out.println("The Strings are both of length " + len1);
			if(s1.equals(s2))
			{
				System.out.println("The Strings are lexicographically the same");
			}
			else
			{
				System.out.println("The Strings are not lexicographically the same");
			}
		}
		else
		{
			System.out.println("The Strings are not the same length");
		}

		char c1 = s1.charAt(2);
		s1 = s1.toUpperCase();
		s2 = s2.toLowerCase();
		System.out.println("S1: " + s1);
		System.out.println("S2: " + s2);

		if(s1.indexOf('e') != -1)
		{
			System.out.println("The character e appears at index: " + s1.indexOf('e'));
		}
	}
}