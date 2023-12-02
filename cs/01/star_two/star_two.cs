using System.Text.RegularExpressions;

partial class Program
{
    static readonly string FILE_LOCATION = "../../../input/day_01.txt";
    static readonly Regex reNumbers = MyRegex();
    static readonly Dictionary<string, string> NUMBERS = new()
    {
        { "one", "o1e" },
        { "two", "t2o" },
        { "three", "t3e" },
        { "four", "f4r" },
        { "five", "f5e" },
        { "six", "s6x" },
        { "seven", "s7n" },
        { "eight", "e8t" },
        { "nine", "n9e" }
    };

    static void Main(string[] args)
    {
        string[] arr = File.ReadAllLines(FILE_LOCATION);

        int total = arr.Aggregate(0, (sum, line) => {
            foreach (var key in NUMBERS.Keys)
            {
                line = line.Replace(key, NUMBERS[key]);
            };

            var matchedNumbers = reNumbers.Matches(line)
                .OfType<Match>()
                .Select(m => m.Groups[0].Value)
                .ToArray();

            int num = int.Parse(matchedNumbers.First() + matchedNumbers.Last());
            return sum + num;
        });

        Console.WriteLine(total);
    }

    [GeneratedRegex(@"[0-9]")]
    private static partial Regex MyRegex();
}