import password_hasher


def main() -> None:
    # Хешування паролю
    hashed = password_hasher.hash_password("my_secure_password")
    print("Hashed password:", hashed)

    # Перевірка паролю
    is_valid = password_hasher.verify_password("my_secure_password", hashed)
    print("Is valid:", is_valid)


if __name__ == "__main__":
    main()

