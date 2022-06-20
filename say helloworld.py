text = input("Say anything ?: ")
#1
def helloworld(str1: str = 'Hello, world !', i : int = 0, a : int = 10):
	return (print(str1, "created LazzyZzJob's") for q in range(i, a))
helloworld(text)
#2
x1 = lambda str1 = "Hello, world !", i = int(1), a = int(10) : (print(str1, "created LazzyZzJob's") for q in range(i, a))
x1(text)
