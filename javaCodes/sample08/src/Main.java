public class Main {

    public static void main(String[] args) {

        String[] ogrenciler = new String[4];
        ogrenciler[0]="Engin";
        ogrenciler[1]="Ali";
        ogrenciler[2]="Doguhan";
        ogrenciler[3]="Aybars";

        for(int i=0;i< ogrenciler.length;i++){
            System.out.println(ogrenciler[i]);
        }

        for(String ogrenci:ogrenciler) {
            System.out.println(ogrenci);
        }









    }
}
