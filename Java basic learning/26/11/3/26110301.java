public class stringMethods1
{
	public static void main(String args[])
	{
		String s1 = new String("Hello World");
		System.out.println("s1: " + s1);

		System.out.println("s1 in lowercase: " + s1.toLowerCase());
		System.out.println("s1 now: " + s1);  //put in after
		System.out.println("s1 in uppercase: " + s1.toUpperCase());

		System.out.println("s1 now: " + s1); //put in after


		String s3 = new String("This is an example of a String");
		System.out.println("s3: " + s3);

		System.out.println("s3 in uppercase: " + s3.toUpperCase());
		System.out.println("s3 in lowercase: " + s3.toLowerCase());
		System.out.println("The length of s3 is: " + s3.length());

		int len = s3.length();
		System.out.println("The length of s3 is: " + len);

		char firstChar = s3.charAt(0);
		System.out.println("The first character in the String " + s3 + " is: " + firstChar);

		char fifthChar = s3.charAt(4);
		System.out.println("The first character in the String " + s3 + " is: " + fifthChar);

		char lastChar = s3.charAt(29);
		System.out.println("The first character in the String " + s3 + " is: " + lastChar);

		lastChar = s3.charAt(s3.length()-1);
		System.out.println("The first character in the String " + s3 + " is: " + lastChar);

	}
}