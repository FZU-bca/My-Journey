package lecture8;

public class evenOdd
{
	public static void main(String args[])
	{
		int num1 = 1, num2 = 899, num3 = 651;
		if(num1 % 2 ==0 && num2 %2 == 0 && num3 % 2 == 0)
		{
			System.out.println("All even");
		}
		else if(num1 % 2 !=0 && num2 %2 != 0 && num3 % 2 != 0)
		{
			System.out.println("All odd");
		}
		else
		{
			System.out.println("Mixed");
		}
	}
}