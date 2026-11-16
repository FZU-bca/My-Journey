public class Bca26111601 {
    public static void main(String args[]){
        int num1=17,num2=9;
        if(num1>num2){
            System.out.println("num1 larger than num2");
        } else if (num1==num2) {
            System.out.println("num1 equals to num2");

        }else{
            System.out.println("num1 smaller than num2");
        }
        int num_1=54;
        int num_2=num1/10;
        int num_3=num1%10;
        if(num_2>num_3){
            System.out.println("in descending order");
        } else if (num_2<num_3) {
            System.out.println("in ascending order");
        }else{
            System.out.println("has equivalent digits");
        }


    }


}
