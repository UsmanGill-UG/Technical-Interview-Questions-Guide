const fs = require('fs');

const getAPIData = async (url) => {
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`Network response was not ok: ${response.status} ${response.statusText}`);
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('There has been a problem with your fetch operation:', error);
        throw error; 
    }
};

const operationsMapping = {
    'FOO' : (arr) => arr.reduce((sum, item) => item + sum, 0),
    'FOX' : (arr) => arr.length ? Math.max(...arr) : undefined,
    'BAR' : (arr) => arr.length ? Math.min(...arr) : undefined,
}

const processLostWorld = async (inputFile) => {

    const fileData = fs.readFileSync(inputFile, 'utf-8');
    const tripdata = await getAPIData(`https://www.jsonkeeper.com/${fileData}`);
    const data = tripdata.data;
    const maskGrouping = {};

    data.timelines.map((item, index) => {

        let mask = data.masks[index];

        if(!maskGrouping[mask]){
            maskGrouping[mask] = [item]
        } else {
            maskGrouping[mask].push(item)
        }
    
    })

    let subops = data.action_plan.sub_operations;
    let finalOp = data.action_plan.operation;
    results = [];

    for(mg in maskGrouping){
        let op = subops[mg];
        let arr = maskGrouping[mg];
        results.push(operationsMapping[op](arr)); 
    }

    let ans = operationsMapping[finalOp](results);
    console.log(ans);
}

const inputFile = process.argv[2];
processLostWorld(inputFile);