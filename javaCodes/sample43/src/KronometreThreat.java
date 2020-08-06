public class KronometreThreat implements Runnable{

    private Thread thread;
    private String threadName;

    public KronometreThreat(String threadName){
        this.threadName = threadName;
        System.out.println("OLUŞTURULUYOR: " + threadName);
    }

    @Override
    public void run() {
        System.out.println("Çalıştırılıyor: " + threadName);

        try{
        for(int i=1 ; i<10 ; i++){
            System.out.println(threadName + " : " + i);
            Thread.sleep(1000);
        }}
        catch (InterruptedException exception){
            System.out.println("KESİLDİ: " +threadName);
        }

        System.out.println("threat bitti: " + threadName);

    }
    public  void start(){
        System.out.println("thread nesnesi oluşuyor");
        if(thread==null){
            thread = new Thread(this,threadName);
            thread.start();
        }
    }
}
