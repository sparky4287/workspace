public class Weapon
{
    /* Class variable */
    private static String name = "";
    private static String type = "";
    private static int heat = 0;
    private static int damage = 0;
    private static double tonnage = 0.0;
    private static int ammo_multiplier = 0;
    private static int min_range = 0;
    private static int sho_range = 0;
    private static int med_range = 0;
    private static int lon_range = 0;
    private static int ext_range = 0;

    /* Constructor */
    public Weapon(String newName,String newType,int newHeat,int newDamage,int newTonnage,int newAmmo_Multiplier,int newMinimum_Range,int newShort_Range,int newMedium_Range,int newLong_Range,int newExtreme_Range)
    {

        /* Initialize the instance variables to the given values */
        setName(newName);
        setType(newType);
        setHeat(newHeat);
        setDamage(newDamage);
        setTonnage(newTonnage);
        setAmmo_Multiplier(newAmmo_Multiplier);
        setMinimum_Range(newMinimum_Range);
        setShort_Range(newShort_Range);
        setMedium_Range(newMedium_Range);
        setLong_Range(newLong_Range);
        setExtreme_Range(newExtreme_Range);
    }

    /* Accessors */
    public String getName(){return name;}
    public String getType(){return type;}
    public int getHeat(){return heat;}
    public int getDamage(){return damage;}
    public double getTonnage(){return tonnage;}
    public int getAmmo_Multiplier(){return ammo_multiplier;}
    public int getMinimum_Range(){return min_range;}
    public int getShort_Range(){return sho_range;}
    public int getMedium_Range(){return med_range;}
    public int getLong_Range(){return lon_range;}
    public int getExtreme_Range(){return ext_range;}

    /* Mutators (Not required for pre-designed weapons) */
    public static void setName(String newName){name = newName;}
    public void setType(String newType){type = newType;}
    public void setHeat(int newHeat){heat = newHeat;}
    public void setDamage(int newDamage){damage = newDamage;}
    public void setTonnage(double newTonnage){tonnage = newTonnage;}
    public void setAmmo_Multiplier(int newAmmo_Multiplier){ammo_multiplier = newAmmo_Multiplier;}
    public void setMinimum_Range(int newMinimum_Range){min_range = newMinimum_Range;}
    public void setShort_Range(int newShort_Range){sho_range = newShort_Range;}
    public void setMedium_Range(int newMedium_Range){med_range = newMedium_Range;}
    public void setLong_Range(int newLong_Range){lon_range = newLong_Range;}
    public void setExtreme_Range(int newExtreme_Range){ext_range = newExtreme_Range;}

    /* Functionality Methods */

    /* Convert Weapon information to String and display */
    public String toString() {
        String s = "";
        s = s + "\nName                  : " + name;
        s = s + "\nType                  : " + type;
        s = s + "\nHeat                  : " + heat;
        s = s + "\nDamage                : " + damage;
        s = s + "\nTonnage               : " + tonnage;
        s = s + "\nAmmo Multiplier       : " + ammo_multiplier;
        s = s + "\nMinimum Range         : " + min_range;
        s = s + "\nShort Range           : " + sho_range;
        s = s + "\nMedium Range          : " + med_range;
        s = s + "\nLong Range            : " + lon_range;
        s = s + "\nExtreme Range         : " + ext_range;
        return s;
    }
}