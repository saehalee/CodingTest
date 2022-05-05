import java.util.Scanner;
class Main{
    public static void main(String [] args) {
      Scanner sc = new Scanner(System.in);
      int h = sc.nextInt();
      int m = sc.nextInt();
      int time = sc.nextInt();
      m += time%60;
      if(m > 59){
        h++;
        m -= 60;
        }
      h += time/60;
      if(h > 23) h -= 24;
      System.out.print(h+" "+ m);
    }
}