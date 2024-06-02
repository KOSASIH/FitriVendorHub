import { User } from '../models/User';
import { VendorService } from '../services/VendorService';
import { UserService } from '../services/UserService';
import { logger } from '../utils/logger';
import { Request, Response } from 'express';
import { v4 as uuidv4 } from 'uuid';

export class UserController {
  async getUsers(req: Request, res: Response) {
    try {
      const userService = new UserService();
      const users = await userService.getUsers();
      res.status(200).json(users);
    } catch (error) {
      logger.error(error);
      res.status(500).json({ message: 'Internal server error' });
    }
  }

  async getUserById(req: Request, res: Response) {
    try {
      const id = req.params.id;
      const userService = new UserService();
      const user = await userService.getUserById(id);
      if (!user) {
        return res.status(404).json({ message: 'User not found' });
      }
      res.status(200).json(user);
    } catch (error) {
      logger.error(error);
      res.status(500).json({ message: 'Internal server error' });
    }
  }

  async createUser(req: Request, res: Response) {
    try {
      const userData = req.body;
      const userService = new UserService();
      const user = await userService.createUser(userData);
      res.status(201).json(user);
    } catch (error) {
      logger.error(error);
      res.status(500).json({ message: 'Internal server error' });
    }
  }

  async updateUser(req: Request, res: Response) {
    try {
      const id = req.params.id;
      const userData = req.body;
      const userService = new UserService();
      const user = await userService.updateUser(id, userData);
      if (!user) {
        return res.status(404).json({ message: 'User not found' });
      }
      res.status(200).json(user);
    } catch (error) {
      logger.error(error);
      res.status(500).json({ message: 'Internal server error' });
    }
  }

  async deleteUser(req: Request, res: Response) {
    try {
      const id = req.params.id;
      const userService = new UserService();
      const result = await userService.deleteUser(id);
      if (result.affectedRows === 0) {
        return res.status(404).json({ message: 'User not found' });
      }
      res.status(200).json({ message: 'User deleted successfully' });
    } catch (error) {
      logger.error(error);
      res.status(500).json({ message: 'Internal server error' });
    }
  }

  async getUsersByVendorId(req: Request, res: Response) {
    try {
      const id = req.params.id;
      const vendorService = new VendorService();
      const users = await vendorService.getUsersByVendorId(id);
      res.status(200).json(users);
    } catch (error) {
      logger.error(error);
      res.status(500).json({ message: 'Internal server error' });
    }
  }

  async createUserForVendor(req: Request, res: Response) {
    try {
      const vendorId = req.params.id;
      const userData = req.body;
      const vendorService = new VendorService();
      const user = await vendorService.createUserForVendor(vendorId, userData);
      res.status(201).json(user);
    } catch (error) {
      logger.error(error);
      res.status(500).json({ message: 'Internal server error' });
    }
  }

  async getUserByIdForVendor(req: Request, res: Response) {
    try {
      const vendorId = req.params.vendorId;
      const userId = req.params.userId;
      const vendorService = new VendorService();
      const user = await vendorService.getUserByIdForVendor(vendorId, userId);
      if (!user) {
        return res.status(404).json({ message: 'User not found' });
      }
      res.status(200).json(user);
    } catch (error) {
      logger.error(error);
      res.status(500).json({ message: 'Internal server error' });
    }
  }

  async updateUserForVendor(req: Request, res: Response) {
    try {
      const vendorId = req.params.vendorId;
      const userId = req.params.userId;
      const userData = req.body;
      const vendorService = new VendorService();
      const user = await vendorService.updateUserForVendor(vendorId, userId, userData);
      if (!user) {
        return res.status(404).json({ message: 'User not found' });
      }
      res.status(200).json(user);
    } catch (error) {
      logger.error(error);
      res.status(500).json({ message: 'Internal server error' });
    }
  }

  async deleteUserForVendor(req: Request, res: Response) {
    try {
      const vendorId = req.params.vendorId;
      const userId = req.params.userId;
      const vendorService = new VendorService();
      const result = await vendorService.deleteUserForVendor(vendorId, userId);
      if (result.affectedRows === 0) {
        return res.status(404).json({ message: 'User not found' });
      }
      res.status(200).json({ message: 'User deleted successfully' });
    } catch (error) {
      logger.error(error);
      res.status(500).json({ message: 'Internal server error' });
    }
  }
}
