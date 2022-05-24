def helloworld(str: str = 'Hellow, world !', i : int = 0, a : int = 10):
	q = [print(str, "create LazzyJob's") for q in range(i, a)]
	return str, i, a, q

helloworld()
