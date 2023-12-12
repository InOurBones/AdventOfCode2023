import * as fs from "fs/promises";
import * as path from "path";

const DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];
const ADJECENT = [
    [-1, -1], [0, -1], [1, -1],
    [-1, 0], [1, 0],
    [-1, 1], [0, 1], [1, 1]
];

let gears: number[][] = []
function mapSymbolsToDict(lines: string[]) {
    for (let i = 0; i < lines.length; i++) {
        const characters = Array.from(lines[i]);
        for (let j = 0; j < characters.length; j++) {
            if (characters[j] == "*") {
                gears.push([i, j])
            }
        }
    }
}

function adjecentNumber(numbers: any[][], xg: number, yg: number): number[] {
    let tmp = []
    for (const [number, positions] of numbers) {
        for (const [a, b] of ADJECENT) {
            const postToCheck = [xg + a, yg + b]
            const posIncludes = positions.some(
                (r: number[]) => r.every((value, index) => postToCheck[index] == value)
            )  // we can ignore the r.length check because we only store arrays with 2 values
            if (posIncludes) {
                tmp.push(parseInt(number))
                break
            }
        }
    }
    return tmp
}

(async () => {
    const rawInput = await fs.readFile(path.resolve(__dirname, '../../input/day_03.txt'), "utf-8");
    const arr = rawInput.split("\n");

    mapSymbolsToDict(arr)
    
    let k = ""
    let pos: number[][] = []
    let numbers = []
    for (let i = 0; i < arr.length; i++) {

        if (k != "") {
            numbers.push([k, pos])
            k = ""
            pos = []
        }

        for (let j = 0; j < arr[i].length; j++) {
            const c = arr[i][j];
            if (k != "" && !DIGITS.includes(c)) {
                numbers.push([k, pos])
                k = ""
                pos = []
            }

            if (DIGITS.includes(c)) {
                k += c
                pos.push([i, j])
            }
        }
    }

    const total = gears.reduce((sum, gear) => {
        const x = adjecentNumber(numbers, gear[0], gear[1])
        return sum + ( x.length == 2 ? (x[0] * x[1]) : 0 )
    }, 0)
    console.log(total)
})();