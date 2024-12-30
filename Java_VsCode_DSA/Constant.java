public class Constant {

    // Static method to demonstrate constant time complexity
    static void ConstantTime() {
        int array[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
        System.out.println(array[0]); // Print the first element of the array
    }

    // Static method to demonstrate linear time complexity
    static void LinearTime() {
        int array[] = {1, 2, 3, 4, 5, 6899, 7, 8, 9};
        for (int i = 0; i < array.length; i++) {
            System.out.println(array[i]); // Print all elements of the array
        }
    }

    // Main method
    public static void main(String[] args) {
        Constant.ConstantTime(); // Call the ConstantTime method
        Constant.LinearTime();   // Call the LinearTime method
    }
}
