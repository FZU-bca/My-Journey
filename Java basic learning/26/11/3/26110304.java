public class phoneNumber
{
	public static void main(String args[])
	{
		String num = new String("353874123122"), international = new String(""), operator = new String(""), number = new String("");
		international = num.substring(0,3);
		operator = num.substring(3,5);
		number = num.substring(5);

		System.out.println("The international code is: " + international);
		System.out.println("The operator code is: " + operator);
		System.out.println("The number is: " + number);

		System.out.println("The complete telephone number is: (" + international + ") " + operator + " " + number);
	}
}