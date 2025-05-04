file_name = input("File name: ").lower().strip()

extension = file_name.split(".").pop()

match extension:
    case "gif" | "jpeg" | "png":
        print(f"image/{extension}")
    case "jpg":
        print("image/jpeg")
    case "txt":
        print("text/plain")
    case "pdf" | "zip":
        print(f"application/{extension}")
    case _:
        print("application/octet-stream")
