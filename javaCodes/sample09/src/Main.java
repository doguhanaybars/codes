public class Main {

    public static void main(String[] args) {

        double[] mylist = {1.2, 3.2, 4.2, 5.2};
        double total = 0;
        double max = mylist[0];
        for (double number : mylist) {
            if (max < number) {
                max = number;
            }
            total = total + number;
            System.out.println(number);
        }
        System.out.println("TOPLAM= " + total);
        System.out.println("EN BÜYÜK SAYI= " + max);
    }
}
