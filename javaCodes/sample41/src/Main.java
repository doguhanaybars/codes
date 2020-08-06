public class Main {

    public static void main(String[] args) {
//        ArrayList<String> sehirler = new ArrayList<String>();
//        sehirler.add("Ankara");
//        sehirler.add("İstanbul");
//        sehirler.add("İzmir");
        MyList<String> sehirler = new MyList<>();
        sehirler.add("Ankara");
        MyList<Customer> sample = new MyList<Customer>();
        sample.add(new Customer());
        sample.add(new Customer());
    }
}
