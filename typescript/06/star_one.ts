import * as fs from "fs/promises";
import * as path from "path";

(async () => {
    const rawInput = await fs.readFile(path.resolve(__dirname, '../../input/day_04.txt'), "utf-8");
    const arr = rawInput.split("\n");
    
})();