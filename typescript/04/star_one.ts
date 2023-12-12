import * as fs from "fs/promises";
import * as path from "path";

(async () => {
    const rawInput = await fs.readFile(path.resolve(__dirname, '../../input/day_04.txt'), "utf-8");
    const arr = rawInput.split("\n");

    const total = arr.reduce((sum, line) => {
        const [winNumsTmp, ownNums] = line.split(":")[1].split("|");
        const winNums = winNumsTmp.split(" ").filter(value => value != "")
        
        let sub_count = 0.5
        ownNums.split(" ").forEach(y => {
            if (winNums.includes(y))
                sub_count *= 2
        })

        return sum + ( sub_count != 0.5 ? sub_count : 0 )
    }, 0)
    console.log(total)
})();