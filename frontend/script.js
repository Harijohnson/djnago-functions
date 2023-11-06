document.getElementById('signin-button').addEventListener('click', function() {
    document.getElementById('overlay').style.display = 'flex';
});

document.getElementById('close-button').addEventListener('click', function() {
    document.getElementById('overlay').style.display = 'none';
});

document.getElementById('signup-button').addEventListener('click', function() {
    alert('Sign Up button clicked');
});

document.getElementById('login-button').addEventListener('click', function() {
    alert('Login button clicked');
});

document.getElementById('signin-button').addEventListener('click', function() {
    document.querySelector('.signin-container').style.display = 'none';
    document.querySelector('.logout-button').style.display = 'block';
});
