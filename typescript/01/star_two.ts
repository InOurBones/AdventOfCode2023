import * as fs from "fs/promises";
import * as path from "path";

const NUMBERS = {
    one: "o1e",
    two: "t2o",
    three: "t3e",
    four: "f4r",
    five: "f5e",
    six: "s6x",
    seven: "s7n",
    eight: "e8t",
    nine: "n9e",
};

(async () => {
    const rawInput = await fs.readFile(path.resolve(__dirname, '../../input/day_01.txt'), "utf-8");
    const arr = rawInput.split("\n");

    const total = arr.reduce((sum, line) => {
        Object.keys(NUMBERS).forEach(key => line = line.replaceAll(key, NUMBERS[key]));

        const number_matches = line.match(/[0-9]/g)!
        const number = parseInt(number_matches.at(0) + number_matches!.at(-1)!);  // assume AOC is fair
        return sum + number;
    }, 0);

    console.log(total);
})();