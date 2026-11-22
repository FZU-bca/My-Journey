public class Bca26112204 {
    public static void main(String[] args){
        int row=0;
        for (row=1;row<=9;row++){
            for(int mul=1;mul<=row;mul++){
                int sum=0;
                sum=row*mul;
                System.out.print(" "+row+"*"+mul+"="+row*mul);
            }
            System.out.println();

        }


    }
}
