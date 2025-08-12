def contador():
    contar = [-1]

    def incrementar():
        contar[0] += 1
        return contar[0]

    return incrementar

def main():
    c = contador()

    for _ in range(10):
        print(f"Contador: {c()}")

if __name__ == "__main__":
    main()