import * as fs from "fs/promises";
import * as path from "path";

function lower(l1: number[], l2: number[]) {
    const minValue = Math.min(l1[0], l2[0])
    const maxValue = Math.max(l1[0], l2[0])
    return maxValue > minValue ? [minValue, maxValue] : []
}

function intersect(l1: number[], l2: number[]) {
    const minIntersect = Math.max(l1[0], l2[0])
    const maxIntersect = Math.min(l1[1], l2[1])
    return minIntersect <= maxIntersect ? [minIntersect, maxIntersect] : []
}

function upper(l1: number[], l2: number[]) {
    const minValue = Math.min(l1[1], l2[1]) + 1
    const maxValue = Math.max(l1[1], l2[1])
    return minValue < maxValue ? [minValue, maxValue] : []
}

function divide(l1: number[], l2: number[]): number[][] {
    return [lower(l1, l2), intersect(l1, l2), upper(l1, l2)]
}

function processMapSeeds(map: [number[], number][], seeds: number[][]): number[][] {
    const ranges = []

    while (seeds.length > 0) {
        const item = seeds.pop()
        const startingLength = ranges.length

        for (let i = 0; i < map.length; i++) {
            const [range, dst]: [number[], number] = map[i];
            const [lower, intersect, upper] = divide(item, range)
            if (intersect.length == 0)
                continue
    
            const diffLower = intersect[0] - range[0]
            const intersectLength = intersect[1] - intersect[0]
            ranges.push([dst + diffLower, dst + diffLower + intersectLength])
    
            if (intersect[0] == item[0] && intersect[1] == item[1])
                break

            if (upper.length == 0 && upper[1] == item[1])
                seeds.push(upper)
            else if (lower.length == 0 && lower[0] == item[0])
                seeds.push(lower)
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

    // load starting ranges
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