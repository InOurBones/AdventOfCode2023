import * as fs from "fs/promises";
import * as path from "path";

const symbolDict = {}
const SYMBOLS = ['#', '$', '%', '&', '*', '+', '-', '/', '=', '@'];
const DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];
const ADJECENT = [
    [-1, -1], [0, -1], [1, -1],
    [-1, 0], [1, 0],
    [-1, 1], [0, 1], [1, 1]
];

function mapSymbolsToDict(lines: string[]) {
    for (let i = 0; i < lines.length; i++) {
        const characters = Array.from(lines[i]);
        for (let j = 0; j < characters.length; j++) {
            if (SYMBOLS.includes(characters[j])) {
                if (Object.prototype.hasOwnProperty.call(symbolDict, i))
                    symbolDict[i][j] = true
                else
                    symbolDict[i] = { [j]: true }
            }
        }
    }
}

function adjecentNumber(pos: number[][], k: string): number {
    for (const [x, y] of pos) {
        for (const [a, b] of ADJECENT) {
            if (Object.prototype.hasOwnProperty.call(symbolDict, (x + a)) &&
                (Object.prototype.hasOwnProperty.call(symbolDict[x + a], (y + b))))
                return Number(k)
        }
    }
    return 0
}

(async () => {
    const rawInput = await fs.readFile(path.resolve(__dirname, '../../input/day_03.txt'), "utf-8");
    const arr = rawInput.split("\n");

    mapSymbolsToDict(arr)
    
    let k = ""
    let pos: number[][] = []
    let total = 0
    for (let i = 0; i < arr.length; i++) {

        if (k != "") {
            total += adjecentNumber(pos, k)
            k = ""
            pos = []
        }

        for (let j = 0; j < arr[i].length; j++) {
            const c = arr[i][j];
            if (SYMBOLS.includes(c) || c == ".") {
                total += adjecentNumber(pos, k)
                k = ""
                pos = []
            }

            if (DIGITS.includes(c)) {
                k += c
                pos.push([i, j])
            }
        }
    }

    console.log(total)
})();