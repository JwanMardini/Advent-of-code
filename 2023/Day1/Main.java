import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Main {

    private static final String FILE_PATH = "2023/Day1/data.txt";
    private static final Map<String, String> TEXT_TO_NUM = new HashMap<>();

    static {
        TEXT_TO_NUM.put("one", "1");
        TEXT_TO_NUM.put("two", "2");
        TEXT_TO_NUM.put("three", "3");
        TEXT_TO_NUM.put("four", "4");
        TEXT_TO_NUM.put("five", "5");
        TEXT_TO_NUM.put("six", "6");
        TEXT_TO_NUM.put("seven", "7");
        TEXT_TO_NUM.put("eight", "8");
        TEXT_TO_NUM.put("nine", "9");
    }

    public static void main(String[] args) {
        int result = 0;
        try (BufferedReader br = new BufferedReader(new FileReader(FILE_PATH))) {
            String line;
            while ((line = br.readLine()) != null) {
                String converted = convert(line.trim());
                char[] separatedArray = converted.replaceAll("[^0-9]", "").toCharArray();
                for (char c : separatedArray) {
                    System.out.print(c);
                }
                System.out.println();
                String numericVal = separatedArray[0] + separatedArray[separatedArray.length - 1];
                
                
            }
            System.out.println(result);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static String convert(String text) {
        for (String key : TEXT_TO_NUM.keySet()) {
            text = text.replace(key, TEXT_TO_NUM.get(key));
        }
        return text;
    }
}
