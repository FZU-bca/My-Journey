public class Bca26112205 {
    public static void main(String[] args){
        int begin_num=100;
        int sum=0;
        int i=0;
        for(begin_num=100;begin_num<=999;begin_num++){
            if(begin_num/100==begin_num%10){
                System.out.print(" "+begin_num);
                sum+=begin_num;
                i++;
            }

        }
        System.out.println();
        System.out.println(sum);
        System.out.println();
        System.out.println(i);
    }
}
