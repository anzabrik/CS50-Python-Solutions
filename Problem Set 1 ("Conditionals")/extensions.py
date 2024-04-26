filename = input("Name of the file: ")

# delete everything before .
filename = filename.lower().strip()

f_list = filename.split(".")
filename = f_list[-1]
filename = "." + filename



match filename:
    case ".gif":
        print("image/gif")
    case ".jpg" | ".jpeg":
        print("image/jpeg")
    case ".png":
        print("image/png")
    case ".pdf":
        print("application/pdf")
    case ".txt":
        print("text/plain")
    case ".zip":
        print("application/zip")
    case _:
        print("application/octet-stream")
