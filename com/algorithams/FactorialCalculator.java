public class FactorialCalculator {
    public static void main(String[] args) {
        int number = 5; // Change this value to calculate the factorial of a different number
        long factorial = calculateFactorial(number);
        System.out.println("The factorial of " + number + " is " + factorial);
    }

    public static long calculateFactorial(int n) {
        if (n == 0) {
            return 1;
        }
        return n * calculateFactorial(n - 1);
    }
}