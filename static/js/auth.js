function showLogout() {
    loginForm.style.display = 'none';
    authLink.textContent = 'Выйти';
    authLink.addEventListener('click', function() {
        localStorage.removeItem('loggedIn');
        location.reload();
    });
}