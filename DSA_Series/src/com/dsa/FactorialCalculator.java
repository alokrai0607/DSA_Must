package com.dsa;

//public class FactorialCalculator {
//
//	public static long factorial(long n) {
//		if (n < 0) {
//			throw new IllegalArgumentException("Here is Negative Number");
//		}
//
//		long fact = 1;
//
//		for (int i = 1; i <= n; i++) {
//			fact *= i;
//		}
//
//		return fact;
//
//	}
//
//	public static void main(String[] args) {
//		long number = 5;
//		long result = factorial(number);
//		System.out.println(result);
//
//	}
//
//}


//WAy-2

public class FactorialCalculator {

    public static long factorial(int n) {
        // Base case: if n is 0 or 1, return 1
        if (n == 0 || n == 1) {
            return 1;
        }
        // Recursive case: multiply n by factorial of (n - 1)
        else {
            return n * factorial(n - 1);
        }
    }

    public static void main(String[] args) {
        int number = 5; // Example number
        long result = factorial(number);
        System.out.println("Factorial of " + number + " is: " + result);
    }
}

