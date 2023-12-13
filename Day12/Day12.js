// operational (.) or damaged (#) unknown (?)
//the size of each contiguous group of damaged springs is listed in the order those groups appear in the row
// how many different arrangements of operational and broken springs fit the given criteria in each row

const fs = require('fs');

const filePath = 'ex.txt';
const lines = [];
const springs = [];
const clues = [];

function replaceQuestionMarks(str) {
    const combinations = [];

    function backtrack(index, currentCombination) {
        if (index === str.length) {
            combinations.push(currentCombination);
            return;
        }

        if (str[index] === "?") {
            backtrack(index + 1, currentCombination + "#");
            backtrack(index + 1, currentCombination + ".");
        } else {
            backtrack(index + 1, currentCombination + str[index]);
        }
    }

    backtrack(0, "");
    return combinations;
}

fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }
    
    lines.push(...data.split('\n'));
    const extractedDigits = lines.map(line => {
        const digits = line.match(/\d+(,\d+)*/g);
        return digits ? digits[0].split(',') : [];
    });

    const extractedCharacters = lines.map(line => line.match(/[?.#]*/g)[0] || []);
    
    // console.log(lines);
    
    // console.log(springs);
    console.log(lines[0]);

    
    console.log(extractedDigits);
    console.log(extractedCharacters[0]);
    const combos0 = replaceQuestionMarks(extractedCharacters[0])
    contiguous_damaged = combos0.map(combo => combo.match(/(#+)(?!$)/g));//.map(match => match.length));
    const continguous_damaged_lengths = contiguous_damaged.map(matches => matches.map(match => match.length));


    console.log(combos0);
    console.log();

    // console.log(extractedCharacters);
});

// console.log(lines[0]);
// console.log(replaceQuestionMarks(lines[0]);