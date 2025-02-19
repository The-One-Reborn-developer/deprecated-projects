import express from "express";
import { Request, Response } from "express";

import { validateTelegramData } from "../modules/common_index.js";
import { insertUser } from "../modules/queries_index.js";

const commonRouter = express.Router();
commonRouter.use(express.json());

commonRouter.post(
  "/validate-init-data",
  async (req: Request, res: Response) => {
    const pool = req.app.get("pool");
    const initData = req.body;

    try {
      const urlEncodedInitData = new URLSearchParams(initData).toString();

      const result = validateTelegramData(urlEncodedInitData);

      if (!result.isValid) {
        res
          .status(result.status)
          .json({ message: result.message, isValid: result.isValid });
        return;
      }

      if (typeof result.message === "object" && result.message.user) {
        const userData = result.message.user;
        const insertUserResult = await insertUser(pool, userData);

        console.log(`
          Insert user status: ${insertUserResult.status},
          Insert user message: ${insertUserResult.message},
          Insert user data: ${insertUserResult.data}
        `);

        res.status(insertUserResult.status).json({
          message: insertUserResult.message,
          data: insertUserResult.data,
        });

        return;
      }
    } catch (error) {
      console.error(`Error in /common/validate-init-data: ${error}`);
    }
  }
);

export default commonRouter;
