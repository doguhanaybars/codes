import java.io.*;


public class Main {

    public static void main(String[] args) {
        BufferedReader reader = null;
        int total = 0;
        try {

            reader = new BufferedReader(new FileReader("C:\\Users\\AYBARS\\Desktop\\codes\\javaCodes\\sample38\\src\\sayilar.txt"));
            String line = null;
            while ((line = reader.readLine()) != null) {
                total += Integer.valueOf(line);

            }
            System.out.println("Toplam: " + total);
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            try {
                reader.close();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }
}
