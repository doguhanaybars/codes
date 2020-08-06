import java.util.ArrayList;

public class Main {

    public static void main(String[] args) {
        ArrayList<Customer> customers = new ArrayList<>();
        customers.add((new Customer(1,"Ali","Kuas")));
        customers.add((new Customer(2,"Aybars","Ay")));
        customers.add((new Customer(3,"Kaan","Çetin")));

        for( Customer customer : customers) {
            System.out.println(customer.firstName);
        }

    }
}
