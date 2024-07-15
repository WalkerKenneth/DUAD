document.getElementById('login').addEventListener('submit', function (e) {
    e.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    fetch('data/users.json')
        .then(response => response.json())
        .then(users => {
            const user = users.find(u => u.username === username && u.password === hashPassword(password));
            if (user) {
                localStorage.setItem('loggedInUser', JSON.stringify(user));
                showTodoList();
            } else {
                alert('Invalid username or password');
            }
        });
});

document.getElementById('logout').addEventListener('click', function () {
    localStorage.removeItem('loggedInUser');
    showLoginForm();
});

function showLoginForm() {
    document.getElementById('login-form').style.display = 'block';
    document.getElementById('todo-list').style.display = 'none';
}

function showTodoList() {
    document.getElementById('login-form').style.display = 'none';
    document.getElementById('todo-list').style.display = 'block';
}

function hashPassword(password) {
    return btoa(password);
}

if (localStorage.getItem('loggedInUser')) {
    showTodoList();
} else {
    showLoginForm();
}
