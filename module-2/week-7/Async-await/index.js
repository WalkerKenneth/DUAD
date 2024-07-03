async function requestUser(number) {
    try{
        const user = await fetch(`https://reqres.in/api/users/${number}`);
        const userData = await user.json();

        return userData.data;
    } catch (error){
        return 'Error getting user data';
    }
}

async function getData(){
    let user_index = document.getElementById('user_index').value;
    let userData = await requestUser(user_index);
    user_info = document.getElementById("user_info");

    user_info.innerHTML = `
            <p>Name: ${userData.first_name} ${userData.last_name}</p>
            <p>Email: ${userData.email}</p>
            <img src="${userData.avatar}" alt="User Avatar">
        `;
}

document.getElementById("submit").addEventListener("click", getData);