import { BaseController } from './baseController';
import { UserService } from '../services/userService';

export class UserController extends BaseController {
  private userService: UserService;

  constructor(req: Request, res: Response, next: NextFunction) {
    super(req, res, next);
    this.userService = new UserService();
  }

  async getUsers() {
    try {
      const users = await this.userService.getUsers();
      this.res.json(users);
    } catch (error) {
      this.handleError(error);
    }
  }
}
