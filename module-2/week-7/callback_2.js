//Second Exercise
const fs = require('fs');

fs.readFile('module-2/week-7/data-1.txt', 'utf8', (err, data1) => {
    if (err) {
        console.error(err);
        return;
    }
    console.log('First file content:', data1);
    array_1 = data1.split("\n");

    fs.readFile('module-2/week-7/data-2.txt', 'utf8', (err, data2) => {
        if (err) {
            console.error(err);
            return;
        }
        console.log('Second file content:', data2);
        array_2 = data2.split("\n");

        let duplicates = array_1.filter(value => array_2.includes(value));
        console.log(duplicates);
    });
});