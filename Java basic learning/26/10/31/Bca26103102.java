public class Bca26103102 {
    public static void main(String[] args) {
        Bca26103102 cbc = new Bca26103102();
        cbc.checkColour('F', 1);
        cbc.checkColour('G', 7);
        cbc.checkColour('J', 1);
    }

    private void checkColour(char letter, int num) {
        char upperLetter = Character.toUpperCase(letter);
        if (upperLetter < 'A'||upperLetter>'H'||num<1||num>8) {
            System.out.println("Wrong code");
            return;
        }
        int colNumber=upperLetter-'A'+1;
        if ((colNumber+num)%2==0){
            System.out.println("Light");
        }
        else{
            System.out.println("Dark");
        }
    }
}