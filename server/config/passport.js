const LocalStrategy = require('passport-local').Strategy;
const User = require('../models/User');

module.exports = function (passport) {
  passport.use(
    new LocalStrategy((username, password, done) => {
      User.findOne({ username }, (err, user) => {
        if (err) return done(err);
        if (!user) return done(null, false, { message: 'Incorrect username.' });

        // Compare the provided password with the stored hash
        // If the passwords match, call `done` with the user object; otherwise, call it with `false`
      });
    })
  );

  passport.serializeUser((user, done) => {
    done(null, user.id);
  });

  passport.deserializeUser((id, done) => {
    User.findById(id, (err, user) => {
      done(err, user);
    });
  });
};
