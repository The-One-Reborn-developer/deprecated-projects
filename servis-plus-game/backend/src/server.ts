import express from "express";
import dotenv from "dotenv";
import { createServer } from "http";
import pkg from "pg";

import commonRoute from "./routes/common.js";

import { createUsersTable } from "./modules/queries_index.js";
import { initializeWebsocketServer } from "./modules/common_index.js";

dotenv.config({ path: "/app/.env" });

const app = express();
app.use(express.json());
app.use("/api/common", commonRoute);

const httpServer = createServer(app);
const SERVER_PORT = process.env.PORT || 3000;
const POSTGRES_PORT = parseInt(process.env.POSTGRES_PORT ?? "5432", 10);

const { Pool } = pkg;
const pool = new Pool({
  user: process.env.POSTGRES_USER,
  password: process.env.POSTGRES_PASSWORD,
  database: process.env.POSTGRES_DB,
  port: POSTGRES_PORT,
  host: process.env.POSTGRES_HOST,
});
app.set("pool", pool);
const sendMessageToUser = initializeWebsocketServer(httpServer);

async function initializeDatabase() {
  const createUsersTableQuery = createUsersTable();
  try {
    await pool.query(createUsersTableQuery);
    console.log("Users table created successfully or already exists.");
  } catch (error) {
    console.error("Error creating users table:", error);
    process.exit(1);
  }
}

async function startServer() {
  await initializeDatabase();

  httpServer.listen(SERVER_PORT, () => {
    console.log(`Server running on port ${SERVER_PORT}`);
  });
}

startServer();
