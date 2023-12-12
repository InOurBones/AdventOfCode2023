import * as fs from "fs/promises";
import * as path from "path";

(async () => {
    const rawInput = await fs.readFile(path.resolve(__dirname, '../../input/day_05.txt'), "utf-8");
    const arr = rawInput.split("\n\n");

    const [seeds, ...maps] = arr;
    const seedsArr = seeds.split(": ")[1].split(" ").map(Number)
    let seedsDict: {[key: number]: number} = seedsArr.reduce((acc, val) => ({ ...acc, [val]: val }), {});

    maps.forEach(x => {
        x.split("\n").slice(1).forEach(y => {
            const [dstStart, srcStart, rng] = y.split(" ").map(Number)

            Object.keys(seedsDict).forEach(seed => {
                const seedInt = Number(seed)  // behind the scenes, keys are parsed as strings
                if (seedInt >= srcStart && seedInt <= srcStart + rng - 1)
                    seedsDict[seed] = dstStart + (seedInt - srcStart)
            })
        })

        seedsDict = Array.from(Object.values(seedsDict)).reduce((acc, val) => ({ ...acc, [val]: val }), {})
    })
    const total = Math.min(...Object.values(seedsDict))
    console.log(total)
})();