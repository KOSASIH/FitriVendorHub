import swaggerUi from 'wagger-ui-express';
import swaggerJsdoc from 'wagger-jsdoc';

const options = {
  definition: {
    openapi: '3.0.0',
    info: {
      title: 'FitriVendorHub API',
      version: '1.0.0',
      description: 'API for FitriVendorHub',
    },
    servers: [
      {
        url: 'http://localhost:3000/api',
      },
    ],
  },
  apis: ['./routes/*.js'],
};

const swaggerSpec = swaggerJsdoc(options);

export const swaggerUiMiddleware = swaggerUi.serve;
export const swaggerUiOptions = swaggerUi.setup(swaggerSpec);
