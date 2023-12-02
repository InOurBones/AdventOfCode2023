import * as fs from "fs/promises";
import * as path from "path";

(async () => {
    const rawInput = await fs.readFile(path.resolve(__dirname, '../../input/day_02.txt'), "utf-8");
    const arr = rawInput.split("\n");

    const total = arr.reduce((sum, line) => {
        const input = line.split(": ")[1].replaceAll(",", ";")
        let inventory = {}

        for (const s of input.split("; ")) {
            const count = parseInt(s.split(" ")[0])
            const cube = s.split(" ")[1]

            if (!Object.prototype.hasOwnProperty.call(inventory, cube) || count > inventory[cube])
                inventory[cube] = count
        }
        const num = Object.values(inventory).reduce((a: number, b: number) => a * b, 1) as number

        return sum + num;
    }, 0);

    console.log(total);
})();