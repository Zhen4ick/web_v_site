document.addEventListener("DOMContentLoaded", function() {
    const authLink = document.getElementById('authLink');
    if (localStorage.getItem('loggedIn') === 'true') {
        check();
    }
    function check() {
        authLink.textContent = 'Выход';
        authLink.addEventListener('click', function() {
            localStorage.removeItem('loggedIn');
            location.reload();
        });
    }
});