import crypto from 'crypto';

export function generateRandomToken() {
  return crypto.randomBytes(16).toString('hex');
}
