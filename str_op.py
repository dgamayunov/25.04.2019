s='У лукоморья 123 дуб зелёный 456'
print('буква "я" по счёту ', s.find('я'))
print('буква "у" встречается', s.count('у'), 'раз(а)')
if s.isalpha is not True:
    print(s.upper())
else:
    print (s)
if len(s) > 4:
    print (s.lower())
print(s.replace("У","О"))