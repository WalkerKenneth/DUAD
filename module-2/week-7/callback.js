//First exercise
function numberType(number, evenFunction, oddFunction){
    if (number % 2 === 0){
        evenFunction();
    }
    else {
        oddFunction();
    }
}

const evenFunction = () => {
    console.log("The number is even!");
};

const oddFunction = () => {
    console.log("The number is odd!")
};

numberType(5, evenFunction, oddFunction);