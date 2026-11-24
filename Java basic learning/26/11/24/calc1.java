package lecture10;

public class calc1
{
	public static void main(String args[])
	{
		String s1 = new String(""), s2 = new String(""), s3 = new String("");
		int num1 = 0 , num2 = 0;
		char operator = ' ';
		s1 = args[0];
		s2 = args[1];
		s3 = args[2];
		
		num1 = Integer.parseInt(s1);
		num2 = Integer.parseInt(s3);
		operator = s2.charAt(0); //using what they know by now
		if(operator == '+')
		{
			System.out.println(num1 + " + " + num2 + " = " + (num1+num2));
		}
		else if(operator == '-')
		{
			System.out.println(num1 + " - " + num2 + " = " + (num1-num2));
		}
		else if(operator == 'x') //cant use * as it is a special character
		{
			System.out.println(num1 + " x " + num2 + " = " + (num1*num2));
		}
		else if(operator == '/')
		{
			System.out.println(num1 + " / " + num2 + " = " + (num1/num2));
		}
		else
		{
			System.out.println("invalid character entered"); // dont use $ % etc
		}
	}
}