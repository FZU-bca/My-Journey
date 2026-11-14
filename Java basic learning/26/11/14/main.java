public class main{
        public static void main(String[] args){
        String Wordslist="abcdefghijklmnopqrstuvwxyz";
        String Transformation="pqeynbiskathcuzrdofljgmvxw";
        String result="";
        String formalMessage="p apgp roziopc cjfl spgn zun zo czon ehpffnf lsn upcn zb lsn fzjoen bkhn puy lsn upcn zb lsn ehpff cjfl qn lsn fpcn kb mn mpul cptn p apgp roziopc nvnejlpqhn mn cjfl rozgkyn p cpku cnlszy lsn cpku cnlszy kf pu kuykeplzo puy p fkiupljon bzo apgp gkoljph cpeskun lz bkuy lsn nulox rzkul zb lsn roziopc bzo nvnejlkzu";
        for(int i = 0 ; i < formalMessage.length() ; i++){
                char currentMessage=formalMessage.charAt(i);
                if (currentMessage == ' '){
                        result += ' ';
                }
                else{
                        int position = Transformation.indexOf(currentMessage);
                        char Truemessage = Wordslist.charAt(position);
                        result += Truemessage;



                }

        }
System.out.println(result);

        }

        }