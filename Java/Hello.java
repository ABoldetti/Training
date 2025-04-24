public class Hello {
    public static void main( String[] argv){
        System.out.println("Hello world");
    }
}

public class prime{
    public static void main(String[] args) {
        int n = 10;
        boolean isPrime = true;

        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                isPrime = false;
                break;
            }
        }

        if (isPrime && n > 1) {
            System.out.println(n + " is a prime number.");
        } else {
            System.out.println(n + " is not a prime number.");
        }
    }
}