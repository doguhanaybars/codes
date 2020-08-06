import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;

public class Main {

    public static void main(String[] args) {
        ArrayList<String> sehirler = new ArrayList<String>();
        sehirler.add("Ankara");
        sehirler.add("Bursa");
        sehirler.add("İzmir");
        sehirler.add("Aydın");
        System.out.println(sehirler);
        sehirler.remove("Ankara");
        Collections.sort(sehirler); //sıralar
        for(String i : sehirler){
            System.out.println(i);
        }
    }
}
