//imports
const fs = require("fs");

//global variables
const filename = process.argv[2];

const numToWord = {
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine",
    0 : "zero"
}

const delemiters = [' ', '-', '+', '(', ')']

//program starts here
fs.readFile(filename, 'utf-8', (err, data) => {

    if(err)
        throw err;
    
    data = data.split(/\r?\n/).slice(1);
    const numberToSentence = {} //mapping of phone number to an array of reading ways
    data.forEach(item => processString(numberToSentence, item));

    let fileContent = '';
    data.forEach(item => {

        const num = extractNumber(item)

        if(!numberToSentence[num].checked){
            fileContent += num + '\n';
            numberToSentence[num].forEach(item => fileContent += item + '\n');
            numberToSentence[num].checked = true;
        }

    })

    fileContent = fileContent.slice(0, -1); //removes last '\n'
    fs.writeFile('output.txt', fileContent, err => {
        if(err)
            throw err;
    });
})

const processString = (numberToSentence, inputString) => {

    const number = extractNumber(inputString);
    const sentence = getSentence(inputString);

    if(!numberToSentence[number])
        numberToSentence[number] = [sentence]
    else if(!numberToSentence[number].includes(sentence))
        numberToSentence[number].push(sentence);

}


//helper functions
const extractNumber = (inputString) => { //function to get actual number, removing any delimeters

    let result = ''
    for(const char of inputString){
        if(!delemiters.includes(char)){
            result += char;
        }
    }

    return result;
}



const CountPerChar = (count, char) => {

    char = numToWord[char];

    if(count > 10)
        return char.repeat(count - 1);

    const counts = [
        "one", "double", "triple", "quadruple", "quintuple",
        "sextuple", "septuple", "octuple", "nonuple", "decuple"
    ];

    return count === 1 ? char : counts[count - 1] + ' ' + char;

}

const getSentence = (inputString) => {

    let i = 0, count = 1;
    //count contains the number of times a specific number occurs consecutively
    // console.log(inputString)

    let sentence = []
    while(i != inputString.length){

        if(delemiters.includes(inputString[i])){
            i++;
            continue;
        }
            
        if(inputString[i] === inputString[i+1]){
            count++;
        } else {
            sentence.push(CountPerChar(count, inputString[i]));
            count = 1;
        }

        i++;
        
    }

    return sentence.join(' ');

}

