import subprocess
import sys


if __name__ == '__main__':
    version = sys.argv[1]
    result = subprocess.run(['helloworld_cli'], stdout=subprocess.PIPE)
    
    test_str = f"Version: {version}\nHello, world!\n"
    print(test_str.encode())
    print(result.stdout.decode("utf-8").encode())
    res = result.stdout.decode("utf-8") == test_str
    print("1/1 Test #1: ", "Passed" if res else "Fail")
    exit(0 if res else 1)