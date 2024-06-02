import dotenv from 'dotenv';

dotenv.config();

const envConfig = {
  NODE_ENV: process.env.NODE_ENV,
  PORT: process.env.PORT,
  MONGO_URL: process.env.MONGO_URL,
  MONGO_DB_NAME: process.env.MONGO_DB_NAME,
  MONGO_USERNAME: process.env.MONGO_USERNAME,
  MONGO_PASSWORD: process.env.MONGO_PASSWORD,
  SEQUELIZE_URL: process.env.SEQUELIZE_URL,
  SEQUELIZE_DB_NAME: process.env.SEQUELIZE_DB_NAME,
  SEQUELIZE_USERNAME: process.env.SEQUELIZE_USERNAME,
  SEQUELIZE_PASSWORD: process.env.SEQUELIZE_PASSWORD,
  JWT_SECRET: process.env.JWT_SECRET,
  JWT_EXPIRES_IN: process.env.JWT_EXPIRES_IN,
};

export default envConfig;
