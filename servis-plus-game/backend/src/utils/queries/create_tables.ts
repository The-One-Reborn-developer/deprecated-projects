export function createUsersTable() {
  return `CREATE TABLE IF NOT EXISTS users_dev (
    id SERIAL PRIMARY KEY,
    telegram_id BIGINT NOT NULL UNIQUE,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL,
    language_code VARCHAR(2) NOT NULL,
    is_premium BOOLEAN NOT NULL,
    allows_write_to_pm BOOLEAN NOT NULL,
    photo_url TEXT
  );`;
}
