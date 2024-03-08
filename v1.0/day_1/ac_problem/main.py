def get_t(tr, tc, mode):
	if mode == "heat" and tc > tr:
		return tc
	elif mode == "freeze" and tc < tr:
		return tc
	elif mode == "auto":
		return tc
	return tr


tr, tc = map(int, input().split())
mode = input()

print(get_t(tr, tc, mode))
