import * as fs from "fs/promises";
import * as path from "path";

function findIntersect(l1: number[], l2: number[]) {
    const minIntersect = Math.max(l1[0], l2[0])
    const maxIntersect = Math.min(l1[1], l2[1])
    return minIntersect <= maxIntersect ? [minIntersect, maxIntersect] : []
}

function processMapSeeds(map: [number[], number][], seeds: number[][]): number[][] {
    const ranges = []

    while (seeds.length > 0) {
        const item = seeds.pop()
        const startingLength = ranges.length

        for (let i = 0; i < map.length; i++) {
            const [range, dst]: [number[], number] = map[i];
            const intersect = findIntersect(item, range)
            if (intersect.length == 0)
                continue
    
            const diffLower = intersect[0] - range[0]
            const intersectLength = intersect[1] - intersect[0]
            ranges.push([dst + diffLower, dst + diffLower + intersectLength])
    
            if (intersect[0] == item[0] && intersect[1] == item[1])
                break
        }

        if (startingLength == ranges.length)
            ranges.push(item)
    }

    return ranges
}

(async () => {
    const rawInput = await fs.readFile(path.resolve(__dirname, '../../input/day_05.txt'), "utf-8");
    const arr = rawInput.split("\n\n");

    const [seeds, ...maps] = arr;
    const seedsArr = seeds.split(": ")[1].split(" ").map(Number)

    let seedRanges: number[][] = []
    for (let i = 0; i < seedsArr.length; i+=2) {
        seedRanges.push([seedsArr[i], seedsArr[i] + seedsArr[i + 1] - 2])
    }
    
    maps.forEach(map => {
        const parsedMap: [number[], number][] = map.split("\n").slice(1).map(line => {
            const [dst, src, l] = line.split(" ").map(Number)
            const range = [src, (src + l - 1)]
            return [range, dst]
        })
       
        seedRanges = processMapSeeds(parsedMap, seedRanges)
    })
    const total = Math.min(...seedRanges.map(x => x[0]))
    console.log(total)
})();