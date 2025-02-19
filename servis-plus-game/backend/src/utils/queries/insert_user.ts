interface JSON {
  [key: string]: any;
}

export async function insertUser(pool: any, userData: string): Promise<any> {
  try {
    if (!userData) {
      return {
        status: 400,
        message: "Invalid user data",
      };
    }

    const parsedUserData = JSON.parse(userData);

    const insertUserQuery = `INSERT INTO users_dev (
    telegram_id,
    first_name,
    last_name,
    username,
    language_code,
    is_premium,
    allows_write_to_pm,
    photo_url
  ) VALUES ($1, $2, $3, $4, $5, $6, $7, $8)
  ON CONFLICT (telegram_id) DO UPDATE
  SET
    first_name = EXCLUDED.first_name,
    last_name = EXCLUDED.last_name,
    username = EXCLUDED.username,
    language_code = EXCLUDED.language_code,
    is_premium = EXCLUDED.is_premium,
    allows_write_to_pm = EXCLUDED.allows_write_to_pm,
    photo_url = EXCLUDED.photo_url
  RETURNING *`;

    const insertUserValues = [
      parsedUserData.id,
      parsedUserData.first_name,
      parsedUserData.last_name,
      parsedUserData.username,
      parsedUserData.language_code,
      parsedUserData.is_premium,
      parsedUserData.allows_write_to_pm,
      parsedUserData.photo_url,
    ];
    const insertUserResult = await pool.query(
      insertUserQuery,
      insertUserValues
    );

    return {
      status: 200,
      message: "User inserted or updated successfully",
      data: JSON.stringify(insertUserResult.rows[0]),
    };
  } catch (error) {
    console.error(`Error in insertUser: ${error}`);
    return { status: 500, message: "Database error" };
  }
}
