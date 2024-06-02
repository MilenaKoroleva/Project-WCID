const loginBtn = document.getElementById('login-btn');
const registerBtn = document.getElementById('register-btn');
const loginForm = document.querySelector('.login-form');
const registrationForm = document.querySelector('.registration-form');

registerBtn.addEventListener('click', function() {
    loginForm.classList.add('hidden');
    registrationForm.classList.remove('hidden');
    loginBtn.classList.remove('active');
    registerBtn.classList.add('active');
});

loginBtn.addEventListener('click', function() {
    registrationForm.classList.add('hidden');
    loginForm.classList.remove('hidden');
    registerBtn.classList.remove('active');
    loginBtn.classList.add('active');
});

loginForm.addEventListener('submit', function(e) {
    e.preventDefault();
});

registrationForm.addEventListener('submit', function(e) {
    e.preventDefault();
});