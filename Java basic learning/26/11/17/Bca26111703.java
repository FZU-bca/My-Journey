public class Bca26111703 {
    public static void main(String[]args){
        int sumDiv=0;
        int sumSqa=0;
        for(int i=1;i<=100;i++){
            if((i%13)==0)sumDiv+=1;
            sumSqa+=i*i;
        }
        System.out.println("The sum of all numbers divisible by 13 is"+sumDiv);
        System.out.print("The sum of all squares is"+sumSqa);


    }



}
