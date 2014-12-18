public class Hero {

    /* Class variable */
    private static String name;
    private static int char_class;
    private static int life_pts;
    private static int tech_pts;
    private static int power;
    private static int hit_rate;

    /* Initial Default Constructor */
    public Hero() {
        name = "";
        char_class = 0;
        life_pts = 0;
        tech_pts = 0;
        power = 0;
        hit_rate = 0;
    }

    /* Constructor Part Two (Copies new input values on top of default Hero constructor) */
    public Hero(String newName, int newChar_Class, int newLife_Pts, int newTech_Pts, int newPower, int newHit_Rate) {

        /* Initialize the instance variables to the given values */
        setName(newName);
        setChar_Class(newChar_Class);
        setLife_Pts(newLife_Pts);
        setTech_Pts(newTech_Pts);
        setPower(newPower);
        setHit_Rate(newHit_Rate);
    }

    /* Accessors */
    public String getName() {
        return name;
    }
    public int getChar_Class() {
        return char_class;
    }
    public int getLife_Pts() {
        return life_pts;
    }
    public int getTech_Pts() {
        return tech_pts;
    }
    public int getPower() {
        return power;
    }
    public int getHit_Rate() {
        return hit_rate;
    }

    /* Mutators */
    public static void setName(String newName) {
        if(!newName.equals("")){
            name = newName;
        }
    }
    public void setChar_Class(int newChar_Class) {
        if(newChar_Class > 0){
            char_class = newChar_Class;
        }
    }
    public void setLife_Pts(int newLife_Pts) {
        if(newLife_Pts <= 0){
            life_pts = 0;
        } else {
            life_pts = newLife_Pts;
        }
    }
    public void setTech_Pts(int newTech_Pts) {
        if(newTech_Pts <= 0){
            tech_pts = 0;
        } else {
            tech_pts = newTech_Pts;
        }
    }
    public void setPower(int newPower) {
        if(newPower > 0){
            power = newPower;
        }
    }
    public void setHit_Rate(int newHit_Rate) {
        if(newHit_Rate > 0 && newHit_Rate <= 100){
            hit_rate = newHit_Rate;
        }
    }

    /* Functionality Methods */

    /* Convert Hero character information to String and display */
    public String toString() {
        String s = "";
        s = s + "\nName                  : " + name;
        switch(char_class){
            case 1:
                s = s + "\nClass                 : Warrior";
                break;
            case 2:
                s = s + "\nClass                 : Ranger";
                break;
            case 3:
                s = s + "\nClass                 : Wizard";
                break;
            default:
                break;
        }
        s = s + "\nHealth Points         : " + life_pts;
        s = s + "\nTechnique Points      : " + tech_pts;
        s = s + "\nPower                 : " + (int)(0.75 * power) + "-" + power;
        s = s + "\nHit Rate              : " + hit_rate + "%\n";
        return s;
    }
}