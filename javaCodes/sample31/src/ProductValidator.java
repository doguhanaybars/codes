public class ProductValidator {
    static {
        System.out.println("Statik ÇALIŞTI");
    }

    public ProductValidator(){
        System.out.println("Yapıcı metot ÇALIŞTI");
    }
    public static boolean isValid(Product product){
    if (product.price>0 && !product.name.isEmpty()){
        return true;
    }
    else{
        return false;
    }

    }

}
