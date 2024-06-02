import { Sequelize } from 'equelize';
import { config } from '../config';
import { logger } from '../utils/logger';

const dbUrl = config.DB_URL;
const dbName = config.DB_NAME;
const dbUser = config.DB_USER;
const dbPassword = config.DB_PASSWORD;

const sequelize = new Sequelize(dbUrl, dbUser, dbPassword, {
  dialect: 'postgres',
  host: 'localhost',
  port: 5432,
  logging: false,
  pool: {
    max: 10,
    min: 0,
    idle: 10000,
  },
});

sequelize.authenticate()
 .then(() => {
    logger.info(`Connected to PostgreSQL database: ${dbName}`);
  })
 .catch((error) => {
    logger.error(`Error connecting to PostgreSQL database: ${error}`);
  });

export default sequelize;
