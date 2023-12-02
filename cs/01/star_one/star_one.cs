using System.Text.RegularExpressions;

partial class Program
{
    static readonly string FILE_LOCATION = "../../../input/day_01.txt";
    static readonly Regex reNumbers = MyRegex();

    static void Main(string[] args)
    {
        string[] arr = File.ReadAllLines(FILE_LOCATION);

        int total = arr.Aggregate(0, (sum, line) => {
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