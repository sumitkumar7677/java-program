public class First{
    public static void main(String [] args)
    {
     
        System.out.println("Sumit");
        int num = 10;
        int b = num++;
        System.out.println(b);
        double num_double = num;
        System.out.println(num_double);
        double num2 = 10.9;
        int num3 = (int) num2;
        ++ num3;
        System.out.println(num3);
        String n1 = new String("Sumit");
        String n2 = n1;
        System.out.println(n2);
        System.out.println(num3>num);
        System.out.println(n1.length());
        System.out.println(Math.max(10,20));
        int randomNum = (int)(Math.random() * 101);  // 0 to 100
        System.out.println(randomNum);
        if (num > num3) {
            System.out.println(num + " " + "Is greater than " + " "+ num3);
        }
        else{
            System.out.println(num3 + " "+ "Is Greataer than " +" "+ num);
        }
        String Result = (10>6) ? "10 is greater than 6" : "6 is Greater than 10";
        System.out.println(Result);
        int i = 0;
        while (i < 5) {
        System.out.println(i);
        i++;
}
        int day = 1;
        switch (day)
        {
          case 1:
          System.out.println("Monday");
          break;

          case 2:

          System.out.println("Tuesday");
          break;
        }
        int b2=4;
        while (b2>=0){
            System.out.println(b);
            b2--;
        }
        System.out.println("While loop are executed");

    }
}