public class BCa26112104 {
    public static void main(String[] args){
        int num=5;
        int i=0;
        int total=0;
        for(i=1;i<=num;i++){
            int rowsum=0;
            for(int n=1;n<=i;n++){
                rowsum+=n;
                System.out.print(n+" ");
            }
            System.out.println("    "+rowsum);
            total+=rowsum;

        }
        System.out.println("Total = "+total);



    }
}
