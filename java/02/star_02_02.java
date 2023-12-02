import java.io.File;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Scanner;

public class star_02_02 {
    public static void main(String[] args) {
        try {
            File myFile = new File("./input/day_02.txt");
            Scanner myReader = new Scanner(myFile);
            
            int total = 0;
            while (myReader.hasNextLine()) {
                String input = myReader.nextLine().split(": ")[1].replaceAll(",", ";");
                HashMap<String, Integer> inventory = new HashMap<>();

                for (String s : input.split("; ")) {
                    Integer count = Integer.parseInt(s.split(" ")[0]);
                    String cube = s.split(" ")[1];

                    if (!inventory.containsKey(cube) || count > inventory.get(cube))
                        inventory.put(cube, count);
                }

                int[] arr = Arrays.stream(inventory.values().toArray()).mapToInt(o -> (int)o).toArray();
                total += multiple(arr);
            }

            System.out.println(total);
            myReader.close();
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();            
        }
    }

    static int multiple(int[] arr) {
        int pro = 1;
        for (int i : arr) {
            pro *= i;
        }
        return pro;
    }
}
