//Exercise 1
const printElements = (elements) => {
    for (let i in elements) {
        console.log(elements[i]);
    }
};

//Exercise 2
const evenNumbers = (numberList) => {
    let evenNumbersList = [];
    for (let i in numberList) {
        if (numberList[i] % 2 === 0) {
            evenNumbersList.push(numberList[i]);
        }
    };
    return evenNumbersList;
};

const evenNumbersFilter = (numberList) => {
    const evenCheck = (number) => {
        return number % 2 === 0;
    };
    let evenNumbersList = numberList.filter(evenCheck);
    return evenNumbersList;
};

//Exercise 3
const celsiusToFarenheit = (gradesList) => {
    const farenheit = (grade) => {
        return (grade * 1.8) + 32;
    }
    let gradesF = gradesList.map(farenheit);
    return gradesF;
};

//Exercise 4
const wordList = (text) => {
    let list = [];
    let word = '';
    for (let i in text) {
        if (text[i] === ' ') {
            list.push(word);
            word = ''
        } else if (parseInt(i) === text.length - 1) {
            word += text[i];
            list.push(word);
        }
        else {
            word += text[i];
        };
    };
    return list;
};

//Exercise 5
const studentResume = (student) => {
    let gradesNumber = 0;
    let gradeAvg = 0;
    let highestGrade = '';
    let tempHigh = 0;
    let lowestGrade = '';
    let tempLow = 0;


    for (let key in Object.values(student.grades)) {
        gradesNumber += 1;
        gradeAvg += student.grades[key].grade;

        if (highestGrade === '') {
            highestGrade = student.grades[key].name;
            tempHigh = student.grades[key].grade;
        } else {
            if (student.grades[key].grade > tempHigh) {
                highestGrade = student.grades[key].name;
                tempHigh = student.grades[key].grade;
            }
        }

        if (lowestGrade === '') {
            lowestGrade = student.grades[key].name;
            tempLow = student.grades[key].grade;
        } else {
            if (student.grades[key].grade < tempLow) {
                lowestGrade = student.grades[key].name;
                tempLow = student.grades[key].grade;
            }
        }
    }

    let resume = {
        name: student.name,
        gradeAvg: gradeAvg / gradesNumber,
        highestGrade: highestGrade,
        lowestGrade: lowestGrade,
    };
    return resume;
}

//Exercise 1 test
let names = ['Roberto', 'Carlos', 'Maria'];
printElements(names);

//Exercise 2 test
let numbers = [5, 6, 88, 12, 33, 78, 90, 25];
let evenList = evenNumbers(numbers);
let evenListFilter = evenNumbersFilter(numbers);
console.log(evenList);
console.log(evenListFilter);

//Exercise 3 test
let gradesCelsius = [0, 12, 34, 45, 68, 100];
let gradesFarenheit = celsiusToFarenheit(gradesCelsius);
console.log(gradesFarenheit);

//Exercise 4 test
let text = 'This is a string!';
let words = wordList(text);
console.log(words);

//Exercise 5 test
let student = {
    name: "John Doe",
    grades: [
        { name: "math", grade: 80 },
        { name: "science", grade: 100 },
        { name: "history", grade: 60 },
        { name: "PE", grade: 90 },
        { name: "music", grade: 98 }
    ]
};
let resume = studentResume(student);
console.log(resume);