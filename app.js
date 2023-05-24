const tg = window.Telegram.WebApp;
tg.expand();

const form = document.getElementById("form");

form.addEventListener("submit", (ev) => {
  // убрать page refresh
  ev.preventDefault();

  const name = document.getElementById("name").value;
  const date = document.getElementById("date").value;
  const user_data = {
    name: name,
    date: date,
  };

  tg.sendData(JSON.stringify(user_data));

  tg.close();
});
