import * as fs from "fs/promises";
import * as path from "path";

const INVENTORY = {
    red: 12,
    green: 13,
    blue: 14
}

function gameIsPossible(input: string): boolean {
    for (const s of input.split("; ")) {
        const countNum = parseInt(s.split(" ")[0])
        const cube = s.split(" ")[1]
        if (countNum > INVENTORY[cube]) return false
    }
    return true
}

(async () => {
    const rawInput = await fs.readFile(path.resolve(__dirname, '../../input/day_02.txt'), "utf-8");
    const arr = rawInput.split("\n");

    const total = arr.reduce((sum, line) => {
        const gameNum = parseInt(line.split(": ")[0].substring(5))
        const input = line.split(": ")[1].replaceAll(",", ";")

        return sum + ( gameIsPossible(input) ? gameNum : 0 );
    }, 0);

    console.log(total);
})();