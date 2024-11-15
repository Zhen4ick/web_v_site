document.addEventListener("DOMContentLoaded", function() {
    const loginForm = document.getElementById('loginForm');
    const formLogin = document.getElementById('formLogin');
    const authLink = document.getElementById('authLink');
    const errorMsg = document.getElementById('errorMsg');
    
    // Проверка, авторизован ли пользователь
    if (localStorage.getItem('loggedIn') === 'true') {
        window.location.href = 'index.html';  // Перенаправление на index.html, если уже авторизован
    }

    // Обработчик формы авторизации
    formLogin.addEventListener('submit', function(event) {
        event.preventDefault();
        const login = document.getElementById('login').value;
        const password = document.getElementById('password').value;

        if (login === 'admin' && password === 'admin') {
            localStorage.setItem('loggedIn', 'true');
            window.location.href = 'index.html';  // Перенаправление на index.html после успешного входа
        } else {
            errorMsg.style.display = 'block';
        }
    });
});