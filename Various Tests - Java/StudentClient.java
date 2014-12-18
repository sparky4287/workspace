import java.util.*;
public class StudentClient {
    final static Scanner in = new Scanner(System.in);
    public static void main(String[] args) {

        /*Student s = new Student();
        System.out.println(s);
        System.out.println("\n\n");
        Student s1 = new Student("1234567", "Mary", "Brown", 67);
        System.out.println(s1);

        //s1.units = 100;
        s1.setUnits(100);
        s1.setUnits(-5);
        System.out.println(s1);

        Student s3 = new Student("1234567891", "Frank", "cook", -10);
        System.out.println(s3);*/

        Student[] students = new Student[4];
        for(int a=0; a<3; a++){
            System.out.println("Enter the ID: ");
            String id = in.next();
            System.out.println("Enter the first name: ");
            String name = in.next();
            System.out.println("Enter the last name: ");
            String lName = in.next();
            System.out.println("Enter the number of units: ");
            int units = in.nextInt();
            Student s = new Student(id,name,lName,units);
            students[a] = s;
        }
        for(int b=0; b<3; b++){
            System.out.println("***************\n" + students[b]);
        }
        System.out.println("Enter the ID for the student: ");
        String id = in.next();
        System.out.println("Enter the number of units: ");
        int units = in.nextInt();
        for(int c=0; c<3; c++){
            if(id.equals(students[c].getId())){
                students[c].setUnits(units);
                System.out.println(students[c]);
                //i=4;
            }
        }
    }
}