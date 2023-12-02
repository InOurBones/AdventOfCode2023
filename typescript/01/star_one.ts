import * as fs from "fs/promises";
import * as path from "path";

(async () => {
    const rawInput = await fs.readFile(path.resolve(__dirname, '../../input/day_01.txt'), "utf-8");
    const arr = rawInput.split("\n");

    const total = arr.reduce((sum, line) => {
        const number_matches = line.match(/[0-9]/g)!
        const num = parseInt(number_matches.at(0) + number_matches!.at(-1)!);  // assume AOC is fair
        return sum + num;
    }, 0);

    console.log(total);
})();