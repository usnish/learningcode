#PYTHON VILLAGE PROBLEM #3: Strings and Lists
#Problem
#Given: A string s of length at most 200 letters and four integers a, b, c and d.
#Return: The slice of this string from indices a through b and c through d (with space in between), inclusively.

string = str(raw_input("String?: "))
int1 = int(raw_input("int1? :"))
int2 = int(raw_input("int2? :"))
int3 = int(raw_input("int3? :"))
int4 = int(raw_input("int4? :"))

print string[int1:int2+1] + " " + string[int3:int4+1]