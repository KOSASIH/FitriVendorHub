import mongoose, { Document, Model, Schema } from 'mongoose';

export interface User {
  _id: string;
  name: string;
  email: string;
  password: string;
}

const userSchema = new Schema({
  name: { type: String, required: true },
  email: { type: String, required: true, unique: true },
  password: { type: String, required: true },
});

export const User: Model<User> = mongoose.model('User', userSchema);
