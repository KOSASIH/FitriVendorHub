// Import dependencies
const mongoose = require('mongoose');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');

// Define the Rating schema
const ratingSchema = new mongoose.Schema({
  vendor: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'Vendor',
    required: true
  },
  user: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User',
    required: true
  },
  rating: {
    type: Number,
    required: true,
    min: 1,
    max: 5
  },
  review: {
    type: String,
    required: false
  },
  createdAt: {
    type: Date,
    default: Date.now
  },
  updatedAt: {
    type: Date,
    default: Date.now
  }
});

// Define a pre-save hook to hash the rating
ratingSchema.pre('save', function(next) {
  const rating = this;
  bcrypt.hash(rating.rating, 10, function(err, hash) {
    if (err) {
      return next(err);
    }
    rating.rating = hash;
    next();
  });
});

// Define a method to generate a JWT token for the rating
ratingSchema.methods.generateToken = function() {
  const rating = this;
  const token = jwt.sign({ _id: rating._id }, process.env.RATING_SECRET, {
    expiresIn: '1h'
  });
  return token;
};

// Define a method to verify the rating token
ratingSchema.statics.verifyToken = function(token) {
  const rating = this;
  try {
    const decoded = jwt.verify(token, process.env.RATING_SECRET);
    return rating.findById(decoded._id);
  } catch (err) {
    return null;
  }
};

// Create the Rating model
const Rating = mongoose.model('Rating', ratingSchema);

// Export the Rating model
module.exports = Rating;
