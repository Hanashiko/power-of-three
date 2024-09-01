def isPowerOfThree(n: int) -> bool:
    for i in range(32):
        if 3**i == n:
            return True
    return False

def main() -> None:
    print(isPowerOfThree(27))
    print(isPowerOfThree(0))
    print(isPowerOfThree(-1))
    
if __name__ == "__main__":
    main()