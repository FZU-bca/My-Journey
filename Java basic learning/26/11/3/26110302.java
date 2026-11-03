public class stringJoining
{
	public static void main(String args[])
	{
		String s1 = new String("10");
		String s2 = new String("12");
		int num1 = 10, num2 = 12;

		System.out.println("s1 + s2: " + (s1 + s2));

		System.out.println("Num1 + num2: " + (num1 + num2));

		String stars = new String("**********");
		for(int i = 0; i < 10; i++)
		{
			System.out.println(stars);
		}

	}
}