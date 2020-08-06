public class App {
    public static void main(String[] args) throws Exception {
        //Product product = new Product(1,"Laptop","asus",3000,2,"siyah");
        Product product = new Product();
        product.setName("Laptop");
        product.setId(1);;
        product.setDescription("Asus Laptop");
        product.setPrice(5000);
        product.setStockAmount(3);

        ProductManager productManager = new ProductManager();
        productManager.Add(product);

        productManager.Add2(1, "name", "description", 3, 1000);

        System.out.println(product.getKod());
    }
}
