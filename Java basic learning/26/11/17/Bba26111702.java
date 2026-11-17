public class Bba26111702 {
    public static void main(String args[]){
        int num=3;
        int k=0;
        while((num/2)>0){
            k++;
            num/=2;

        }
        System.out.println(k);
        int factorial=17;
        long result=1;
        while(factorial>1){
            result*=factorial;
            factorial--;
        }
        System.out.println("The factorial of"+factorial+"is"+result);







    }
}
