const fs = require('fs');
const filename = process.argv[2];


const createMatrix = () => {

    const matrix = [];
    let letterCharCode = 'A'.charCodeAt(0);

    for(let i=0; i < 6; i++){
        const row = [];

        for(let j=0; j < 5; j++){

            row.push(String.fromCharCode(letterCharCode));

            if(letterCharCode !== 0)
                letterCharCode++;

            if(letterCharCode > 'Z'.charCodeAt(0))
                letterCharCode = 0
        }

        matrix.push(row);
    }

    return matrix;
}

const matrix = createMatrix();

fs.readFile(filename, 'utf-8', (err, data) => {

    if(err)
        throw err;

    data = data.split(' ');
    result = [];
    data.forEach(item => printInstructions(item, result))
    result = result.join("");
    console.log(result)
})

const printInstructions = (word, result) => {

   
    let i = j = 0;
    word = word.split("");

    word.forEach((item) => {

        currentLetter = matrix[i][j];

        while(item != currentLetter){

            if(item > currentLetter && matrix[i].includes(item)){
                result.push('r')
                j++;
            }
            else if(item > currentLetter && !matrix[i].includes(item)){
                result.push('d')
                i++;
            }
            else if(item < currentLetter && matrix[i].includes(item)){
                result.push('l')
                j--;   
            }
            else if(item < currentLetter && !matrix[i].includes(item)){
                result.push('u')
                i--;
            }

            currentLetter = matrix[i][j];

        }

        result.push('#')

    })

}
