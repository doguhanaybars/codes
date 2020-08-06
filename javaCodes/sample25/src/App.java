public class App {
    public static void main(String[] args) throws Exception {
        // BaseLogger[] loggers = new BaseLogger[]{new FileLogger(),new EmailLoogger(),new DatabaseLogger(),new ConsoleLogger()};
        // for (BaseLogger logger:loggers){
        //     logger.Log("log mesajı");
        // }

        CustomerManager customerManager = new CustomerManager(new DatabaseLogger());
        customerManager.add();
    }
}
