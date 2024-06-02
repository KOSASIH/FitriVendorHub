import { UserController } from '../../controllers/userController';
import { UserService } from '../../services/userService';

describe('UserController', () => {
  let userController: UserController;
  let userService: UserService;

  beforeEach(() => {
    userService = new UserService();
    userController = new UserController(null, null, null, userService);
  });

  it('should get users', async () => {
    const users = await userController.getUsers();
    expect(users).toBeInstanceOf(Array);
  });
});
