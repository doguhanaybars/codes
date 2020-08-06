public class Main {

    public static void main(String[] args) {

        char grade = 'C';

        switch (grade) {
            case 'A':
                System.out.println("Mükemmel Geçiniz ");
                break;
            case 'B':
                System.out.println(" Çok güzel Geçtiniz ");
                break;
            case 'C':
                System.out.println("  Geçtiniz ");
                break;
            case 'D':
                System.out.println(" Şartlı Geçtiniz ");
                break;
            case 'F':
                System.out.println(" Kaldınız :( ");
                break;
            default:
                System.out.println("geçersiz not girdiniz");
        }


    }
}
