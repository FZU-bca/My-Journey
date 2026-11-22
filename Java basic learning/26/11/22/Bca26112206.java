public class Bca26112206 {
    public static void main(String[] args){
        int row=1;
        for(row=1;row<=5;row++){
            for(int space=1;space<=5-row;space++){
                System.out.print(" ");
            }
            for(int stars=1;stars<=2*row-1;stars++){
                System.out.print('*');
            }
            for(int space=1;space<=5-row;space++){
                System.out.print(" ");
            }
            System.out.println();

        }

    }
}
