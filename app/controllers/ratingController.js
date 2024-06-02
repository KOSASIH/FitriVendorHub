// Import dependencies
const Rating = require('../models/rating');
const Review = require('../models/review');
const jwt = require('jsonwebtoken');
const bcrypt = require('bcryptjs');

// Define the ratingController
const ratingController = {};

// Create a new rating
ratingController.create = async (req, res) => {
  try {
    const rating = new Rating(req.body);
    const token = await rating.generateToken();
    res.status(201).send({ token });
  } catch (err) {
    res.status(400).send({ error: err.message });
  }
};

// Get all ratings for a vendor
ratingController.getAll = async (req, res) => {
  try {
    const vendorId = req.params.vendorId;
    const ratings = await Rating.find({ vendor: vendorId });
    res.status(200).send(ratings);
  } catch (err) {
    res.status(400).send({ error: err.message });
  }
};

// Get a single rating
ratingController.get = async (req, res) => {
  try {
    const ratingId = req.params.ratingId;
    const rating = await Rating.findById(ratingId);
    if (!rating) {
      return res.status(404).send({ error: 'Rating not found' });
    }
    res.status(200).send(rating);
  } catch (err) {
    res.status(400).send({ error: err.message });
  }
};

// Update a rating
ratingController.update = async (req, res) => {
  try {
    const ratingId = req.params.ratingId;
    const rating = await Rating.findByIdAndUpdate(ratingId, req.body, {
      new: true
    });
    if (!rating) {
      return res.status(404).send({ error: 'Rating not found' });
    }
    res.status(200).send(rating);
  } catch (err) {
    res.status(400).send({ error: err.message });
  }
};

// Delete a rating
ratingController.delete = async (req, res) => {
  try {
    const ratingId = req.params.ratingId;
    await Rating.findByIdAndRemove(ratingId);
    res.status(204).send();
  } catch (err) {
    res.status(400).send({ error: err.message });
  }
};

// Export the ratingController
module.exports = ratingController;
