public class Enemy {

    /* Class variable */
    private static String name;
    private static int life_pts;
    private static int enem_class;
    private static int tech_pts;
    private static int power;
    private static int hit_rate;

    /* Initial Default Constructor */
    public Enemy() {
        name = "";
        enem_class = 0;
        life_pts = 0;
        tech_pts = 0;
        power = 0;
        hit_rate = 0;
    }

    /* Constructor Part Two (Copies new input values on top of default Enemy constructor) */
    public Enemy(int newEnem_Class, int newLife_Pts, int newTech_Pts, int newPower, int newHit_Rate) {

        /* Initialize the instance variables to the given values */
        setName(newEnem_Class);
        setEnem_Class(newEnem_Class);
        setLife_Pts(newLife_Pts);
        setTech_Pts(newTech_Pts);
        setPower(newPower);
        setHit_Rate(newHit_Rate);
    }

    /* Accessors */
    public String getName() {
        return name;
    }
    public int getEnem_Class() {
        return enem_class;
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
    public static void setName(int newEnem_Class) {
        if(newEnem_Class > 0){
            switch(newEnem_Class){
                case 1:
                    name = "Skeleton Warrior";
                    break;
                case 2:
                    name = "Shade";
                    break;
                case 3:
                    name = "Undead Necromancer";
                    break;
                default:
                    break;
            }
        }
    }
    public void setEnem_Class(int newEnem_Class) {
        if(newEnem_Class > 0){
            enem_class = newEnem_Class;
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

    /* Convert Enemy character information to String and display */
    public String toString() {
        String s = "";
        s = s + "\nName                  : " + name;
        s = s + "\nHealth Points         : " + life_pts;
        s = s + "\nTechnique Points      : " + tech_pts;
        s = s + "\nPower                 : " + (int)(0.75 * power) + "-" + power;
        s = s + "\nHit Rate              : " + hit_rate + "%\n";
        return s;
    }
}