const mongoose = require('mongoose');

// Connect to the database
mongoose.connect('mongodb://localhost:27017/fitri-vendor-hub', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Define the User schema and model
const UserSchema = new mongoose.Schema({
  username: String,
  email: String,
  password: String,
});
const User = mongoose.model('User', UserSchema);

// Define the Vendor schema and model
const VendorSchema = new mongoose.Schema({
  name: String,
  description: String,
  products: [
    {
      name: String,
      price: Number,
      quantity: Number,
    },
  ],
});
const Vendor = mongoose.model('Vendor', VendorSchema);

module.exports = {
  User,
  Vendor,
};
