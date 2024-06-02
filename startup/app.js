import express from 'express';
import mongoose from 'mongoose';
import routes from '../routes';
import logger from '../services/logger';

const app = express();

mongoose.connect(config.database.mongoose.url, config.database.mongoose.options);

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.use(routes);

app.listen(config.server.port, () => {
  logger.info(`Server started on port ${config.server.port}`);
});
