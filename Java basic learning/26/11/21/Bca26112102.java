public class Bca26112102 {
    public static void main(String[] argS){
        int i=0;
        int sum=0;
        for(i=0;i<100;i++){
            if(i%3==0){
                sum+=i;
            }
            else if (i%5==0) {
                sum+=i;
                
            }

        }
        System.out.println(sum);


    }
}
