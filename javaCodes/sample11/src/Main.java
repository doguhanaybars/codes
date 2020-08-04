public class Main {

    public static void main(String[] args) {

        String message = "Bugün hava çok güzel.";


        System.out.println(message);

        System.out.println("Eleman Sayısı: " + message.length());
        System.out.println("5. Eleman: " + message.charAt(4)); // elemanı çekip yazdırma
        System.out.println(message.concat(" Yaşasın!")); // birleştirme işlemi
        System.out.println(message.startsWith("B")); // B ile başlıyor true
        System.out.println(message.endsWith("l")); // . ile bittiğinden false
        char[] karakterler = new char[5];
        message.getChars(0,5 ,karakterler,0);
        System.out.println(karakterler);
        System.out.println(message.indexOf("a")); // baştan arar index verir
        System.out.println(message.lastIndexOf("a"));//sondan arar index verir

        System.out.println(message.replace("güzel","kötü"));
        System.out.println(message.replace(" ","_"));
        System.out.println(message.substring(6));
        System.out.println(message.substring(6,10));
        System.out.println("--------------------");
        for (String kelime:message.split(" ")){
            System.out.println(kelime);
        }
        System.out.println("--------------------");

        System.out.println(message.toLowerCase());
        System.out.println(message.toUpperCase());

        String message2 = "      Bosluklu       ";
        System.out.println(message2);
        System.out.println(message2.trim());
    }
}
