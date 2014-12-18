public class Student {

    //list all the instance variables
    private String id;
    private String name;
    private String lName;
    private int units;

    //constructors (1ist establishes the "State of an Object")
    public Student(){
        id = "Undefined";
        name = "undefined";
        lName = "undefined";
        units = 0;
    }

    public Student(String i, String n, String l, int u){
    
        //id =i;
        setId(i);

        //name= n;
        setName(n);

        //lName = l;
        setLName(l);

        //units = u;
        setUnits(u);
    }

    //accessors
    public String getId(){
        return id;
    }
    public String getName(){
        return name;
    }
    public String getLName(){
        return lName;
    }
    public int getUnits(){
        return units;
    }

    //Mutators
    public void setUnits(int u){
        if (u > units)
            units = u;       
        } 

    public void setName(String n){
        name = n;
    }

    public void setLName(String l){
        lName = l;
    }
  
    public void setId(String i){
        if (i.length() == 10)
            id = i;
    }
   
    public String toString(){
        String s ="";
        s = s + "ID = " + id;
        s = s + "\nName = "+ name;
        s = s + "\nLast name = " + lName;
        s = s +"\nUnits = " + units;
        return s;
    }   
}