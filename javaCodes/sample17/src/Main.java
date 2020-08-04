public class Main {

    public static void main(String[] args) {
        sayiBulmaca();

    }

    public static void sayiBulmaca() {

        int[] sayilar = new int[]{1, 2, 5, 6, 9, 0};
        int aranacak = 5;

        boolean varMı = false;

        for (int sayi : sayilar) {
            if (sayi == aranacak) {
                varMı = true;
                break;
            }
        }

        if (varMı) {
            System.out.println("sayımız: "+ aranacak + " Sayı mevcuttur");
        } else {
            System.out.println("sayımız: "+aranacak + " SAYI MEVCUT DEĞİLDİR");
        }

    }
}
