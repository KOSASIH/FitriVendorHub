# FitriVendorHub
A Pi Network payment integrated e-commerce platform

## Introduction
FitriVendorHub is an e-commerce platform that accepts Pi Coin as a payment method. This repository contains the codebase for the platform, which is built using Node.js and integrates with the Pi Network API.

## Features
* Accepts Pi Coin as a payment method
* Integrates with the Pi Network API for payment processing
* Supports multiple payment methods
* User-friendly interface for vendors and customers

## Getting Started
To get started with the platform, follow these steps:

1. Clone the repository: `git clone https://github.com/KOSASIH/FitriVendorHub.git`
2. Install dependencies: `npm install`
3. Configure the Pi Network API credentials in `config/pi-network.js`
4. Start the server: `npm start`

## Payment Flow
The payment flow for the platform is as follows:

1. Create a payment: `pi.createPayment(paymentData)`
2. Store the payment ID in the database
3. Submit the payment to the Pi Blockchain: `pi.submitPayment(paymentId)`
4. Store the transaction ID in the database
5. Complete the payment: `pi.completePayment(paymentId, txid)`

## API Endpoints
The platform exposes the following API endpoints:

* `POST /payments`: Create a new payment
* `GET /payments/:paymentId`: Get a payment by ID
* `POST /payments/:paymentId/submit`: Submit a payment to the Pi Blockchain
* `POST /payments/:paymentId/complete`: Complete a payment

## Contributing
Contributions to the platform are welcome. To contribute, follow these steps:

1. Fork the repository: `git fork https://github.com/KOSASIH/FitriVendorHub.git`
2. Create a new branch: `git branch my-feature`
3. Make changes and commit them: `git commit -m "My feature"`
4. Push the changes: `git push origin my-feature`
5. Create a pull request: `git request-pull origin my-feature`

## License
The platform is licensed under the MIT License. See `LICENSE` for details.
