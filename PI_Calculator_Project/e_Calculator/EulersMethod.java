
//This program is based of the inifite series of 1/(n!) to calculate the number e. 

package PI_Calculator_Project.e_Calculator;

public class EulersMethod {

    public static void main(String[] args) {
        double e = 1;
        double n = 1;
        double next_denom = 1;
        while (true) {
            next_denom *= n;
            e += (1 / next_denom);
            n++;
            System.out.println(e);
        }

    }
}