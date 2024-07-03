const promise1 = new Promise((resolve) => {
    setTimeout(() => {
        resolve("very");
    }, 1000);
});

const promise2 = new Promise((resolve) => {
    setTimeout(() => {
        resolve("dogs");
    }, 2000);
});

const promise3 = new Promise((resolve) => {
    setTimeout(() => {
        resolve("cute");
    }, 3000);
});

const promise4 = new Promise((resolve) => {
    setTimeout(() => {
        resolve("are");
    }, 4000);
});

Promise.all([promise2, promise4, promise1, promise3])
    .then((values) => {
        console.log(values.join(' '));
    })
    .catch((error) => console.error('Error:', error));
