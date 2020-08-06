public class Valudator {
    public<T extends IEntity> void validate(T entity){

        Valudator valudator = new Valudator();
        Customer customer = new Customer();
        valudator.validate(customer);


    }
}
