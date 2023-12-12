const fs = require('fs');

// const filePath = '/Users/matthewmitchell/Documents/Projects/Advent_of_Code_2023/Day1/ex.txt';
const filePath = '/Users/matthewmitchell/Documents/Projects/Advent_of_Code_2023/Day1/input.txt';

fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }

    const lines = data.split('\n');
    let sum = 0; // Initialize sum variable
    lines.forEach((line) => {
        const firstDigit = line.match(/\d/)?.[0];
        const lastDigit = line.match(/\d(?=\D*$)/)?.[0];

        if (firstDigit && lastDigit) {
            const twoDigitNumber = parseInt(firstDigit + lastDigit);
            console.log(`Two-digit number: ${twoDigitNumber}`);
            sum += twoDigitNumber; // Add the twoDigitNumber to the sum
        }
    });

    console.log(`Sum of all two-digit numbers: ${sum}`);
});
