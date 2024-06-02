import { NextFunction, Request, Response } from 'express';

export class BaseController {
  protected req: Request;
  protected res: Response;
  protected next: NextFunction;

  constructor(req: Request, res: Response, next: NextFunction) {
    this.req = req;
    this.res = res;
    this.next = next;
  }

  protected async handleError(error: any) {
    console.error(error);
    this.res.status(500).json({ message: 'Internal Server Error' });
  }
}
