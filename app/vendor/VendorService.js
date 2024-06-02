import { Vendor } from '../models/Vendor';
import { sequelize } from '../config/database';
import { logger } from '../utils/logger';
import { EventEmitter } from 'events';
import { v4 as uuidv4 } from 'uuid';
import { RedisClient } from 'edis';
import { promisify } from 'util';

const redisClient = new RedisClient({ host: 'localhost', port: 6379 });
const getAsync = promisify(redisClient.get).bind(redisClient);
const setAsync = promisify(redisClient.set).bind(redisClient);

export class VendorService extends EventEmitter {
  constructor() {
    super();
    this.cacheTTL = 3600; // 1 hour
  }

  async getVendors() {
    try {
      const cacheKey = 'endors';
      const cachedVendors = await getAsync(cacheKey);
      if (cachedVendors) {
        return JSON.parse(cachedVendors);
      }
      const vendors = await Vendor.findAll();
      await setAsync(cacheKey, JSON.stringify(vendors), 'EX', this.cacheTTL);
      return vendors;
    } catch (error) {
      logger.error(error);
      throw error;
    }
  }

  async getVendorById(id) {
    try {
      const cacheKey = `vendor:${id}`;
      const cachedVendor = await getAsync(cacheKey);
      if (cachedVendor) {
        return JSON.parse(cachedVendor);
      }
      const vendor = await Vendor.findByPk(id);
      if (!vendor) {
        throw new Error('Vendor not found');
      }
      await setAsync(cacheKey, JSON.stringify(vendor), 'EX', this.cacheTTL);
      return vendor;
    } catch (error) {
      logger.error(error);
      throw error;
    }
  }

  async createVendor(vendorData) {
    try {
      const vendor = await Vendor.create(vendorData);
      this.emit('vendorCreated', vendor);
      return vendor;
    } catch (error) {
      logger.error(error);
      throw error;
    }
  }

  async updateVendor(id, vendorData) {
    try {
      const vendor = await this.getVendorById(id);
      await vendor.update(vendorData);
      this.emit('vendorUpdated', vendor);
      return vendor;
    } catch (error) {
      logger.error(error);
      throw error;
    }
  }

  async deleteVendor(id) {
    try {
      const vendor = await this.getVendorById(id);
      await vendor.destroy();
      this.emit('vendorDeleted', vendor);
      return { message: 'Vendor deleted successfully' };
    } catch (error) {
      logger.error(error);
      throw error;
    }
  }

  async getVendorsByStatus(status) {
    try {
      const cacheKey = `vendors:${status}`;
      const cachedVendors = await getAsync(cacheKey);
      if (cachedVendors) {
        return JSON.parse(cachedVendors);
      }
      const vendors = await Vendor.findAll({ where: { status } });
      await setAsync(cacheKey, JSON.stringify(vendors), 'EX', this.cacheTTL);
      return vendors;
    } catch (error) {
      logger.error(error);
      throw error;
    }
  }

  async updateVendorStatus(id, status) {
    try {
      const vendor = await this.getVendorById(id);
      await vendor.update({ status });
      this.emit('vendorStatusUpdated', vendor);
      return { message: 'Vendor status updated successfully' };
    } catch (error) {
      logger.error(error);
      throw error;
    }
  }

  async getVendorCount() {
    try {
      const cacheKey = 'endorCount';
      const cachedCount = await getAsync(cacheKey);
      if (cachedCount) {
        return parseInt(cachedCount, 10);
      }
      const count = await Vendor.count();
      await setAsync(cacheKey, count.toString(), 'EX', this.cacheTTL);
      return count;
    } catch (error) {
      logger.error(error);
      throw error;
    }
  }

  async getVendorRevenue(startDate, endDate) {
    try {
      const cacheKey = `vendorRevenue:${startDate}:${endDate}`;
      const cachedRevenue = await getAsync(cacheKey);
      if (cachedRevenue) {
        return parseFloat(cachedRevenue);
      }
      const revenue = await sequelize.query(
        `SELECT SUM(invoices.total) as revenue FROM vendors
          JOIN invoices ON vendors.id = invoices.vendor_id
          WHERE invoices.created_at BETWEEN :startDate AND :endDate`,
        {
          replacements: { startDate, endDate },
          type: sequelize.QueryTypes.SELECT,
        }
      );
      await setAsync(cacheKey, revenue[0].revenue.toString(), 'EX', this.cacheTTL);
      return revenue[0].revenue;
    } catch (error) {
      logger.error(error);
     throw error;
    }
  }

  async generateVendorReport(vendorId, startDate, endDate) {
    try {
      const vendor = await this.getVendorById(vendorId);
      const revenue = await this.getVendorRevenue(startDate, endDate);
      const report = {
        vendorName: vendor.name,
        revenue,
        startDate,
        endDate,
      };
      return report;
    } catch (error) {
      logger.error(error);
      throw error;
    }
  }
}
