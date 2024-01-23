// operational (.) or damaged (#) unknown (?)
//the size of each contiguous group of damaged springs is listed in the order those groups appear in the row
// how many different arrangements of operational and broken springs fit the given criteria in each row

const fs = require('fs');

// const filePath = 'ex.txt';
const filePath = 'input.txt';
const lines = [];
const springs = [];
const clues = [];

function arraysAreEqual(array1, array2) {
    if (array1.length !== array2.length) {
        return false;
    }
    for (let i = 0; i < array1.length; i++) {
        if (array1[i] !== array2[i]) {
            return false;
        }
    }
    return true;
}
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


function line_variation_count(line) {
    try {
        const extractedCharacters = line.match(/[?.#]*/g)[0] || [];
        const digits = line.match(/\d+(,\d+)*/g)[0].split(',').map(digit => parseInt(digit));
        const combos0 = replaceQuestionMarks(extractedCharacters);

        contiguous_damaged = combos0.map(combo => combo.match(/([#]+)/g));//.map(match => match.length));
        const continguous_damaged_lengths = contiguous_damaged.map(matches => matches.map(match => match.length));
        const nmatching = continguous_damaged_lengths.filter(match => arraysAreEqual(match, digits)).length;
        return nmatching;
    } catch (error) {
        console.log("Error:", error);
        console.log("Line:", line);
    }
}
fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }
    
    lines.push(...data.split('\n').filter(line => line.trim() !== ''));
    // const extractedDigits = lines.map(line => {
    //     const digits = line.match(/\d+(,\d+)*/g);
        
    //     return digits ? digits[0].split(',').map(digit => parseInt(digit)) : [];
    // });

    // const extractedCharacters = lines.map(line => line.match(/[?.#]*/g)[0] || []);
    
    // // console.log(lines);
    
    // // console.log(springs);
    // console.log(lines[0]);

    
    // console.log(extractedDigits[0]);
    // console.log(extractedCharacters[0]);
    // const combos0 = replaceQuestionMarks(extractedCharacters[0])

    // contiguous_damaged = combos0.map(combo => combo.match(/([#]+)/g));//.map(match => match.length));
    // const continguous_damaged_lengths = contiguous_damaged.map(matches => matches.map(match => match.length));
    // const nmatching = continguous_damaged_lengths.filter(match => arraysAreEqual(match, extractedDigits[0])).length;

    // console.log(combos0);
    // console.log(continguous_damaged_lengths);
    // console.log(nmatching);

    const line_variation_counts = lines.map(line_variation_count);
    console.log(line_variation_counts.reduce((a, b) => a + b, 0));

    // console.log(continguous_damaged_lengths[2]);
    // console.log(extractedDigits[0]);
    // console.log(arraysAreEqual(continguous_damaged_lengths[2], extractedDigits[0]));
    // console.log(extractedCharacters);
});

// console.log(lines[0]);
// console.log(replaceQuestionMarks(lines[0]);