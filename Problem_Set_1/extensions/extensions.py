def main():
    filename = input("File name:").strip()
    media = Files(filename)
    print(media)

def Files(f):
    if f.endswith(".gif"):
        return "image/gif"
    elif f.endswith(".jpg") or f.endswith(".jpeg"):
        return "image/jpeg"
    elif f.endswith(".pdf"):
        return "application/pdf"
    elif f.endswith(".png"):
        return "image/png"
    elif f.endswith(".zip"):
        return "application/zip"
    elif f.endswith(".txt"):
        return "text/plain"
    elif f.endswith(".PDF"):
        return "application/pdf"
    else:
        return "application/octet-stream"

main()




