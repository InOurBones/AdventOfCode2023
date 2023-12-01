namespace HelloWorld;

using System;
using System.Collections;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;

class Program
{
    static readonly string fileLocation = "../../../input/day_01.txt";
    static readonly Regex reNumbers = new Regex(@"[0-9]");
    static readonly Dictionary<string, string> NUMBERS = new Dictionary<string, string>()
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
        string[] arr = File.ReadAllLines(fileLocation);

        int total = arr.Aggregate(0, (sum, line) => {
            foreach (var key in NUMBERS.Keys)
            {
                line = line.Replace(key, NUMBERS[key]);
            };

            var matchedNumbers = reNumbers.Matches(line)
                .OfType<Match>()
                .Select(m => m.Groups[0].Value)
                .ToArray();

            int num = Int32.Parse(matchedNumbers.First() + matchedNumbers.Last());
            return sum + num;
        });

        Console.WriteLine(total);
    }
}