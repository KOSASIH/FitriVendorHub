// Import dependencies
const mongoose = require('mongoose');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');

// Define the Review schema
const reviewSchema = new mongoose.Schema({
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
  review: {
    type: String,
    required: true
  },
  rating: {
    type: Number,
    required: true,
    min: 1,
    max: 5
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

// Define a pre-save hook to hash the review
reviewSchema.pre('save', function(next) {
  const review = this;
  bcrypt.hash(review.review, 10, function(err, hash) {
    if (err) {
      return next(err);
    }
    review.review = hash;
    next();
  });
});

// Define a method to generate a JWT token for the review
reviewSchema.methods.generateToken = function() {
  const review = this;
  const token = jwt.sign({ _id: review._id }, process.env.REVIEW_SECRET, {
    expiresIn: '1h'
  });
  return token;
};

// Define a method to verify the review token
reviewSchema.statics.verifyToken = function(token) {
  const review = this;
  try {
    const decoded = jwt.verify(token, process.env.REVIEW_SECRET);
    return review.findById(decoded._id);
  } catch (err) {
    return null;
  }
};

// Create the Review model
const Review = mongoose.model('Review', reviewSchema);

// Export the Review model
module.exports = Review;
