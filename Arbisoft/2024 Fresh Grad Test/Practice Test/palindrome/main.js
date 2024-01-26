const fs = require("fs");
const filename = process.argv[2];

fs.readFile(filename, 'utf-8', (err, data) => {
    if(err)
        console.log(err);

    console.log(isPalindrome(data.toLowerCase()));
})

const isPalindrome = (word) => {

    let left = 0;
    let right = word.length - 1;

    while(left < right){

        if(word[left] !== word[right])
            return 'FALSE';

        left++;
        right--;
    }

    return 'TRUE';

}
