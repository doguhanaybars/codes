public class Main {

    public static void main(String[] args) {

        int sayi1 = 20;
        int sayi2 = 25;
        int sayi3 = 2;

        if(sayi1>sayi2 & sayi1>sayi3){
            System.out.println("SAYI 1 EN BÜYÜKTÜR");
        }
        else if (sayi2>sayi1 & sayi2>sayi3){
            System.out.println("SAYI 2 EN BÜYÜKTÜR");
        }
        else {
            System.out.println("SAYI 3 EN BÜYÜKTÜR");
        }
    }
}
