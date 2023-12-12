import * as fs from "fs/promises";
import * as path from "path";

(async () => {
    const rawInput = await fs.readFile(path.resolve(__dirname, '../../input/day_04.txt'), "utf-8");
    const arr = rawInput.split("\n");

    const totalDict: { [key: number]: number } = {};
    for (let x = 0; x < 196; x++) {
        totalDict[x] = 1;
    }

    for (let idx = 0; idx < arr.length; idx++) {
        const [winNumsTmp, ownNums] = arr[idx].split(":")[1].split("|");
        const winNums = winNumsTmp.split(" ").filter(value => value != "")
        
        let matchCount = 0
        ownNums.split(" ").forEach(y => {
            if (winNums.includes(y))
                matchCount ++;
        })

        for (let i = idx + 1; i <= idx + matchCount; i++) {
            totalDict[i] += totalDict[idx]            
        }
    }
    const total = Object.values(totalDict).reduce((sum, num) => sum + num)
    console.log(total)
})();