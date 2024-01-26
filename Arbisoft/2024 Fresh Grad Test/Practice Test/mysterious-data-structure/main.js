//implement the 3 structures, if push, push into the actual structures, if pop, pop and compare
const fs = require('fs');

class Stack {

    constructor(){
        this.stack = []
    }

    push(item){
        this.stack.push(item);
    }

    pop(){
        return this.stack.pop();
    }
}

class Queue {
    constructor(){
        this.queue = []
    }

    enqueue(item){
        this.queue.push(item);
    }

    dequeue(){
        return this.queue.shift();
    }
}

class PQ {

    constructor(){
        this.PQ = [];
    }

    enqueue(element, priority){

        let item = {element, priority}

        for(let i=0; i < this.PQ.length; i++){

            if(priority < this.PQ[i].priority){
                this.PQ.splice(i, 0, item);
                return
            }
        }

        this.PQ.push(item);
    }

    dequeue(){
        return this.PQ.pop().element;
    }

}

const filename = process.argv[2];
fs.readFile(filename, 'utf-8', (err, data)=>{
    data = data.split(/\r?\n/);

    const numOps = data[0];
    const ops = data.slice(1);

    console.log(identifyDS(numOps, ops));
})

const identifyDS = (numOps, ops) => {

    // console.log(ops);
    // console.log(numOps);

    const stack = new Stack();
    const queue = new Queue();
    const pq = new PQ();

    let val;
    let activeStates = [true, true, true];

    ops.forEach((op) => {

        op = op.split(" ")
        // console.log(op);

        val = +op[1];

        if(op[0] === 'push'){
            
            if(activeStates[0]){
                stack.push(val);
            } 

            if(activeStates[1]){
                queue.enqueue(val);
            }

            if(activeStates[2]){
                pq.enqueue(val, val);
            }

        } else { //pop

            //pop and match, if doesn't match
            let storedVal;
            if(activeStates[0]){
                storedVal = stack.pop();
                (val !== storedVal) ? activeStates[0] = false : null;
            }

            if(activeStates[1]){
                storedVal = queue.dequeue();
                val !== storedVal ? activeStates[1] = false : null;
            }

            if(activeStates[2]){
                storedVal = pq.dequeue();
                val !== storedVal ? activeStates[2] = false : null;
            }

        }
    })

    let count = 0;
    activeStates.forEach(item => item === true? count++ : null)

    if(count === 0)
        return 'IMPOSSIBLE'
    else if(count === 1){
        if(activeStates[0])
            return 'LIFO'
        else if(activeStates[1])
            return 'FIFO'
        else 
            return 'PQ'
    } else if(count > 1){
        return 'NOT SURE'
    }
    
}
