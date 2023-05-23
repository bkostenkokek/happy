let tg = window.Telegram.WebApp;
tg.expand();
let btn = document.getElementById("btn");

btn.addEventListener("click", function() => {
    let name = document.getElementById("name").value;
    let date = document.getElementById("date").value;
    let user_data = {
        name: name,
        date: date
    }
    tg.sendData(JSON.stringify(user_data));
    tg.sendData(name);
    tg.sendData(date);
    tg.close();
}