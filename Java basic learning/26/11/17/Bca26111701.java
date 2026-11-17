public class Bca26111602 {
    public static void main(String args[]){
        double x_1=6,y_1=7,l_1=3;
        double x_2=4,y_2=5,l_2=7;
        if(Math.abs(y_1-y_2)>=(0.5*(l_1=l_2))||Math.abs(x_1-x_2)>=(0.5*(l_1+l_2))){
            System.out.println("The two squares are apart from each other.");
        }
        else if((Math.abs(y_1-y_2)+0.5*l_2)<=0.5*l_1&&(Math.abs(x_1-x_2)+0.5*l_2)<=0.5*l_1){
            System.out.println("Square1 contains Square2.");
        }
        else if((Math.abs(y_1-y_2)+0.5*l_1)<=0.5*l_2&&(Math.abs(x_1-x_2)+0.5*l_1)<=0.5*l_2){
            System.out.println("Square2 contains Square1.");

        }
        else{
            System.out.println("Square1 intersects with Square2.");
        }





    }
}
