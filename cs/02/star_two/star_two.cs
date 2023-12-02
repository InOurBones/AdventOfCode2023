partial class Program
{
    static readonly string FILE_LOCATION = "../../../input/day_02.txt";

    static void Main(string[] args)
    {
        string[] arr = File.ReadAllLines(FILE_LOCATION);

        int total = arr.Aggregate(0, (sum, line) => {
            string input = line.Split(": ")[1].Replace(",", ";");
            Dictionary<string, int> inventory = new(){};

            foreach (var s in input.Split("; "))
            {
                int count = int.Parse(s.Split(" ")[0]);
                string cube = s.Split(" ")[1];

                if (!inventory.ContainsKey(cube) || count > inventory[cube])
                    inventory[cube] = count;
            }
            int num = inventory.Values.Aggregate(1, (a, b) => a * b);
            
            return sum + num;
        });

        Console.WriteLine(total);
    }
}