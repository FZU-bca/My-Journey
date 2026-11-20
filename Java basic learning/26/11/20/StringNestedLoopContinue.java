package lecture8Code;
public class StringNestedLoopContinue {
    public static void main(String[] args) {
        String text = "programming";
        String vowels = "aeiou";
        int consonantCount = 0;

        for (int i = 0; i < text.length(); i++) {
            char c = text.charAt(i);
            boolean isVowel = false;

            for (int j = 0; j < vowels.length(); j++) {
                if (vowels.charAt(j) == c) {
                    isVowel = true;
                    break;  // found it's a vowel ¡ú stop checking vowels
                }
            }

            if (isVowel) {
                continue;  // skip consonants count, move to next char of text
            }
            System.out.println("Consonant: " + c);
            consonantCount++;
        }
        System.out.println("Total consonants: " + consonantCount);
    }
}