import javax.print.DocFlavor;

public class BalanceInsufficentException extends Exception{
    String message ;
    public BalanceInsufficentException(String message) {
        this.message = message;
    }
    @Override
    public String getLocalizedMessage() {
        return this.message;
    }
}
