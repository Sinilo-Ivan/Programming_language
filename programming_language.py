#end - конец программы - написать в документацию!
w = []
c = input()
while c != "end":
    w.append(c)
    c = input()
code = '\n'.join(w)

#реплейсы на питоновские команды
translations = {"variable ": "", "output": "print", "enter": "input", "loop": "while True", "++": " += 1", "--": " -= 1", "false": "False", "true": "True", "when variable": "for", "repeat": "while", "~": "#", "otherwise": "else", "provided that": "if", "array": "range", "otherwise provided that": "elif"}

not_allow = ["print", "input", "while", "for", "if", "else", "elif"]

fl = True

for i in not_allow:
    if i in code:
        print("Неизвестная команда " + i)
        fl = False
if fl:
    for key, value in translations.items():
        code = code.replace(key, value)
    try:
        exec(code)
    except:
        print("Неизвестная ошибка! Пожалуйста, проверьте свой код ещё раз.")
