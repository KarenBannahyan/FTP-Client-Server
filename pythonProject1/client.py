import socket
import os
def list_photos():
    photo_list = [f for f in os.listdir('.') if f.lower().endswith(('.jpg', '.jpeg'))]
    return photo_list

def main():
    server_ip = input("Введите IP адрес сервера: ")
    server_port = int(input("Введите порт сервера: "))

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (server_ip, server_port)
    client_socket.connect(server_address)

    while True:
        photo = input("Введите имя фотографии или /show для отображения списка фотографий: ")
        if photo == '/show':
            photos = list_photos()
            if photos:
                print("Доступные фотографии:")
                for p in photos:
                    print(p)
            else:
                print("Фотографии не найдены.")
            continue

        photo_name = photo + ".jpg"
        if not os.path.exists(photo_name):
            print(f"Фотография '{photo_name}' не существует.")
            continue

        with open(photo_name, 'rb') as file:
            photo_data = file.read()

        client_socket.sendall(photo_data)
        print("Фотография отправлена на сервер")
        break

    client_socket.close()

if __name__ == "__main__":
    main()