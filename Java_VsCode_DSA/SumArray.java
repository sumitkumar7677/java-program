public class SumArray {

    // Method to calculate the sum of array elements
    static int SumArray(int[] array) {
        int sum = 0;
        for (int i = 0; i < array.length; i++) {
            sum += array[i]; // Sum all elements of the array
        }
        return sum; // Return the computed sum
    }

    // Main method to test the SumArray method
    public static void main(String[] args) {
        int[] numbers = {1, 2, 3, 4, 5}; // Example array
        int result = SumArray(numbers);  // Call the SumArray method
        System.out.println("Sum of array elementsss: " + result); // Print the result
    }
}
