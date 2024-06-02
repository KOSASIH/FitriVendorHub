// Import dependencies
const Review = require('../models/review');
const jwt = require('jsonwebtoken');
const bcrypt = require('bcryptjs');

// Define the reviewController
const reviewController = {};

// Create a new review
reviewController.create = async (req, res) => {
  try {
    const review = new Review(req.body);
    const token = await review.generateToken();
    res.status(201).send({ token });
  } catch (err) {
    res.status(400).send({ error: err.message });
  }
};

// Get all reviews for a vendor
reviewController.getAll = async (req, res) => {
  try {
    const vendorId = req.params.vendorId;
    const reviews = await Review.find({ vendor: vendorId });
    res.status(200).send(reviews);
  } catch (err) {
    res.status(400).send({ error: err.message });
  }
};

// Get a single review
reviewController.get = async (req, res) => {
  try {
    const reviewId = req.params.reviewId;
    const review = await Review.findById(reviewId);
    if (!review) {
      return res.status(404).send({ error: 'Review not found' });
    }
    res.status(200).send(review);
  } catch (err) {
    res.status(400).send({ error: err.message });
  }
};

// Update a review
reviewController.update = async (req, res) => {
  try {
    const reviewId = req.params.reviewId;
    const review = await Review.findByIdAndUpdate(reviewId, req.body, {
      new: true
    });
    if (!review) {
      return res.status(404).send({ error: 'Review not found' });
    }
    res.status(200).send(review);
  } catch (err) {
    res.status(400).send({ error: err.message });
  }
};

// Delete a review
reviewController.delete = async (req, res) => {
  try {
    const reviewId = req.params.reviewId;
    await Review.findByIdAndRemove(reviewId);
    res.status(204).send();
  } catch (err) {
    res.status(400).send({ error: err.message });
  }
};

// Export the reviewController
module.exports = reviewController;
