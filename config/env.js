module.exports = {
  NODE_ENV: process.env.NODE_ENV || 'development',
  MONGODB_URI: process.env.MONGODB_URI || 'mongodb://localhost:27017/fitri-vendor-hub',
  SECRET_KEY: process.env.SECRET_KEY || 'secret-key',
};
