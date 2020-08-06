public class Main {

    public static void main(String[] args) {

        int number = 1;
        int remainder = number % 2;
        System.out.println(remainder);
        System.out.println("--------------");

        boolean isPrime = true;

        if (number == 1) {
            System.out.println("Asal değildir" + number);
            return;
        }
        if (number < 1) {
            System.out.println("Geçersiz Sayı");
        }

        for (int i = 2; i < number; i++) {
            if (number % i == 0) {
                isPrime = false;

            }
        }
        if (isPrime == true) { // sadece isPrime de yazılabilir
            System.out.println("Sayı asaldır: " + number);
        } else {
            System.out.println("Sayı asal değildir " + number);
        }

    }


}

