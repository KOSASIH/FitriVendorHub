import { MongoClient } from 'ongodb';
import { Sequelize } from 'equelize';

const databaseConfig = {
  mongo: {
    url: process.env.MONGO_URL,
    dbName: process.env.MONGO_DB_NAME,
    username: process.env.MONGO_USERNAME,
    password: process.env.MONGO_PASSWORD,
  },
  sequelize: {
    url: process.env.SEQUELIZE_URL,
    dbName: process.env.SEQUELIZE_DB_NAME,
    username: process.env.SEQUELIZE_USERNAME,
    password: process.env.SEQUELIZE_PASSWORD,
  },
};

const mongoClient = new MongoClient(databaseConfig.mongo.url, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

const sequelize = new Sequelize(databaseConfig.sequelize.url, {
  dialect: 'postgres',
  logging: false,
});

export const db = {
  mongo: {
    client: mongoClient,
    db: mongoClient.db(databaseConfig.mongo.dbName),
  },
  sequelize: {
    client: sequelize,
    models: sequelize.models,
  },
};

export const connectToDatabase = async () => {
  try {
    await mongoClient.connect();
    await sequelize.authenticate();
    console.log('Connected to database');
  } catch (error) {
    console.error('Error connecting to database:', error);
  }
};

export const disconnectFromDatabase = async () => {
  try {
    await mongoClient.close();
    await sequelize.close();
    console.log('Disconnected from database');
  } catch (error) {
    console.error('Error disconnecting from database:', error);
  }
};
