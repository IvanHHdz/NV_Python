def main():
    with open("README.md", "r", encoding='utf-8') as file:
        contenido = file.read()
    print(contenido)
if __name__ == "__main__":
    main()