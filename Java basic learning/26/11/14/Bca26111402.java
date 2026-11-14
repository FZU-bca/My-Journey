public class Bca26111402 {
    public static void main(String[] args) {
        String vowels="aeiou";
        String text="A Java program must have one or more classes. The name of the source file and the name of the class must be the same. If we want make a Java program executable, we must provide a main method. The main method is an indicator and a signature for Java Virtual Machine to find the entry point of the program for execution.";
        int start=0;
        String result="";
        while(start < text.length()){
            int spaceIndex=text.indexOf(" ",start);
            if(spaceIndex==-1){
               spaceIndex=text.length();
            }
            String word = text.substring(start,spaceIndex);
            if(word.length()>0){
                int j=0;
                boolean hasVowel=false;
                while(j<word.length()){
                    if(vowels.indexOf(word.charAt(j))!=-1){
                       hasVowel=true;
                       break;
                    }
                    j++;
                }
                if(hasVowel){
                    result=word + " " + result;
                }
            }
            start=spaceIndex+1;
        }
        System.out.println(result);


    }
}
