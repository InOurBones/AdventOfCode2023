partial class Program
{
    static readonly string FILE_LOCATION = "../../../input/day_02.txt";
    static readonly Dictionary<string, int> INVENTORY = new()
    {
        {"red", 12},
        {"green", 13},
        {"blue", 14},
    };

    static void Main(string[] args)
    {
        string[] arr = File.ReadAllLines(FILE_LOCATION);

        int total = arr.Aggregate(0, (sum, line) => {
            int gameNum = int.Parse(line.Split(": ")[0].Substring(5));
            string input = line.Split(": ")[1].Replace(",", ";");
            
            return sum + ( GameIsPossible(input) ? gameNum : 0 );
        });

        Console.WriteLine(total);
    }

    static bool GameIsPossible(string input)
    {
        foreach (var s in input.Split("; "))
        {
            int countNum = int.Parse(s.Split(" ")[0]);
            string cube = s.Split(" ")[1];
            if (countNum > INVENTORY[cube]) return false;
        }
        return true;
    }

}