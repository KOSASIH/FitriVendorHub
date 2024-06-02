import mongoose from 'ongoose';
import { config } from '../config';
import { logger } from '../utils/logger';

mongoose.Promise = global.Promise;

const dbUrl = config.DB_URL;
const dbName = config.DB_NAME;
const dbUser = config.DB_USER;
const dbPassword = config.DB_PASSWORD;

const options = {
  useNewUrlParser: true,
  useUnifiedTopology: true,
  useCreateIndex: true,
  useFindAndModify: false,
  autoIndex: true,
  poolSize: 10,
  bufferMaxEntries: 0,
  connectTimeoutMS: 10000,
  socketTimeoutMS: 45000,
};

mongoose.connect(dbUrl, options);

const db = mongoose.connection;

db.on('error', (error) => {
  logger.error(`Error connecting to MongoDB: ${error}`);
});

db.once('open', () => {
  logger.info(`Connected to MongoDB: ${dbName}`);
});

db.on('disconnected', () => {
  logger.info(`Disconnected from MongoDB: ${dbName}`);
});

db.on('reconnected', () => {
  logger.info(`Reconnected to MongoDB: ${dbName}`);
});

export default mongoose;
