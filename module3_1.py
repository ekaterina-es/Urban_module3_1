calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    str1 = len(string)
    str2 = string.upper()
    str3 = string.lower()
    str_info = str1, str2, str3
    return str_info
def is_contains(string, list_to_search):
    count_calls()
    if string.lower() in (item.lower() for item in list_to_search):
        check_result = True
    else:
        check_result = False
    return check_result

print(string_info("Австралия"))
print(string_info("Многозадачность"))
print(is_contains("Urban", ['ban', 'BaNaN', 'urBAN']))
print(is_contains("Река", ["анамнез", "РЕКА", 'ручей']))
print(is_contains("Река", ["анамнез", 'РЕЧКА']))
print(calls)
