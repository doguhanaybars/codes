public class Main {

    public static void main(String[] args) {


        KronometreThreat threat1 = new KronometreThreat("therad1");
        KronometreThreat threat2 = new KronometreThreat("therad2");
        KronometreThreat threat3 = new KronometreThreat("therad3");

        threat1.start();
        threat2.start();
        threat3.start();








    }
}
