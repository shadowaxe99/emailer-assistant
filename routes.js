const express = require('express');
const router = express.Router();

// Home Page
router.get('/', (req, res) => {
  res.render('home');
});

// Login/Signup Page
router.get('/login', (req, res) => {
  res.render('login', { message: req.flash('error') });
});

router.post('/login', passport.authenticate('local', { failureRedirect: '/login', failureFlash: true }), (req, res) => {
  res.redirect('/dashboard');
});

router.get('/signup', (req, res) => {
  res.render('signup', { message: req.flash('error') });
});

router.post('/signup', (req, res) => {
  const newUser = new User({ username: req.body.username, password: req.body.password });

  newUser.save(err => {
    if (err) {
      req.flash('error', 'A user with that username already exists.');
      return res.redirect('/signup');
    }

    passport.authenticate('local')(req, res, function () {
      res.redirect('/dashboard');
    });
  });
});

// Dashboard
router.get('/dashboard', (req, res) => {
  res.render('dashboard');
});

// Email Page
router.get('/email', (req, res) => {
  res.render('email');
});

// Calendar Page
router.get('/calendar', (req, res) => {
  res.render('calendar');
});

// Settings Page
router.get('/settings', (req, res) => {
  res.render('settings');
});

// Help/Support Page
router.get('/help', (req, res) => {
  res.render('help');
});

module.exports = router;