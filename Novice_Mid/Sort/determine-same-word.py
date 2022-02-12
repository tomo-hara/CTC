from typing import List

def is_equal_string(a : List[str], b : List[str]) -> bool:
	if len(a) != len(b):
		return False
	a.sort()
	b.sort()
	for elem_a, elem_b in zip(a, b):
		if elem_a != elem_b:
			return False
	return True

string_a = input()
string_b = input()
print("Yes") if (is_equal_string(list(string_a), list(string_b))) else print("No")