import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class star_01_02 {
    static Pattern reNumbers = Pattern.compile("[0-9]");
    static HashMap<String, String> mapNumbers = new HashMap<>() {{
        put("one", "o1e");
        put("two", "t2o");
        put("three", "t3e");
        put("four", "f4r");
        put("five", "f5e");
        put("six", "s6x");
        put("seven", "s7n");
        put("eight", "e8t");
        put("nine", "n9e");
    }};

    public static void main(String[] args) {
        try {
            File myFile = new File("./input/day_01.txt");
            Scanner myReader = new Scanner(myFile);
            
            int total = 0;
            while (myReader.hasNextLine()) {
                String line = myReader.nextLine();
                
                for (Map.Entry<String, String> entry : mapNumbers.entrySet()) {
                    line = line.replaceAll(entry.getKey(), entry.getValue());
                }
                
                Matcher matcher = reNumbers.matcher(line);
                ArrayList<String> list = new ArrayList<String>();
                while (matcher.find()) {
                    list.add(matcher.group());
                }
                total += Integer.parseInt(list.get(0) + list.get(list.size() - 1));
            }
            
            System.out.println(total);
            myReader.close();
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }
}