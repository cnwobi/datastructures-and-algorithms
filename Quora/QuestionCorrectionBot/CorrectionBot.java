 String questionCorrectionBot(String question){
 question = question
                .trim()
                .concat("?")
                .replace(",",", ")
                .replaceAll("\\s+,",",")
                .replaceAll("\\?+","?")
                .replaceAll("\\s+"," ");
return question.substring(0,1).toUpperCase()+question.substring(1);
}