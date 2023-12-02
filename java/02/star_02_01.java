import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.Scanner;

public class star_02_01 {
    static HashMap<String, Integer> INVENTORY = new HashMap<>(){{
        put("red", 12);
        put("green", 13);
        put("blue", 14);
    }};

    public static void main(String[] args) {
        try {
            File myFile = new File("./input/day_02.txt");
            Scanner myReader = new Scanner(myFile);
            
            int total = 0;
            while (myReader.hasNextLine()) {
                String line = myReader.nextLine();

                Integer gameNum = Integer.parseInt(line.split(": ")[0].substring(5));
                String input = line.split(": ")[1];

                if (gameIsPossible(input))
                    total += gameNum;
            }

            System.out.println(total);
            myReader.close();
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();            
        }
    }

    static boolean gameIsPossible(String input) {
        for (String s : input.replaceAll(",", ";").split("; ")) {
            Integer count = Integer.parseInt(s.split(" ")[0]);
            String cube = s.split(" ")[1];

            if (count > INVENTORY.get(cube))
                return false;
        }
        return true;
    }
}
