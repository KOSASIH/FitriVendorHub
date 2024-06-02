import jwt from 'jsonwebtoken';
import bcrypt from 'bcrypt';

const jwtSecret = process.env.JWT_SECRET;
const jwtExpiresIn = process.env.JWT_EXPIRES_IN;

const generateToken = (user) => {
  const token = jwt.sign(user, jwtSecret, { expiresIn: jwtExpiresIn });
  return token;
};

const verifyToken = (token) => {
  try {
    const decoded = jwt.verify(token, jwtSecret);
    return decoded;
  } catch (error) {
    return null;
  }
};

const hashPassword = (password) => {
  const salt = bcrypt.genSaltSync(10);
  const hash = bcrypt.hashSync(password, salt);
  return hash;
};

const comparePassword = (password, hash) => {
  return bcrypt.compareSync(password, hash);
};

export { generateToken, verifyToken, hashPassword, comparePassword };
