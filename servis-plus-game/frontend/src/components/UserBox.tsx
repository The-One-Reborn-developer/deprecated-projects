function UserBox({ username }: { username: string }) {
  return (
    <>
      <img src="/user.png" alt="user" />
      <label>{username}</label>
    </>
  );
}

export default UserBox;
