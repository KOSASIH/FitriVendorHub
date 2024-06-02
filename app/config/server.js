import express from 'express';
import helmet from 'helmet';
import cors from 'cors';
import compression from 'compression';
import { connectToDatabase } from './database';
import { envConfig } from './env';
import routes from '../routes';

const app = express();

app.use(helmet());
app.use(cors());
app.use(compression());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.use('/api', routes);

const port = envConfig.PORT || 3000;

app.listen(port, () => {
  console.log(`Server started on port ${port}`);
  connectToDatabase();
});
