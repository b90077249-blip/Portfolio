const btn = document.getElementById("theme");

btn.onclick = () => {
    document.body.classList.toggle("light");

    if (document.body.classList.contains("light")) {
        btn.innerHTML = "☀️";
    } else {
        btn.innerHTML = "🌙";
    }
};
