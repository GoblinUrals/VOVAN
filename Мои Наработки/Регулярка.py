import re

def phone(dr, str):
    for i in dr.split('\n'):
        if str in i:
            her = ''.join(i.split(str))
            her_u = re.findall(r'<(\w+ \w+)>|<(\w+)>|<(\w+ \w+\'\w+)>',her)
            q = [x for x in her_u[0] if len(x)>0]
            her_w = re.sub(r'<(\w+ \w+)>|<(\w+)>|<(\w+ \w+\'\w+)>',' ', her)
            her_q = re.sub(r'\W+[,+$;/ !].\s+', '', her_w.strip('!+, */'))
#         else:
#             return (f"Error => Not found: {str}")
    return (f"Phone => {str}, Name => {''.join(q)}, Address => {her_q.strip('')}")




dr = ("/+1-541-754-3010 156 Alphand_St. <J Steeve>\n 133, Green, Rd. <E Kustur> NY-56423 ;+1-541-914-3010;\n"
"+1-541-984-3012 <P Reed> /PO Box 530; Pollocksville, NC-28573\n :+1-321-512-2222 <Paul Dive> Sequoia Alley PQ-67209\n"
"+1-741-984-3090 <Peter Reedgrave> _Chicago\n :+1-921-333-2222 <Anna Stevens> Haramburu_Street AA-67209\n"
"+1-111-544-8973 <Peter Pan> LA\n +1-921-512-2222 <Wilfrid Stevens> Wild Street AA-67209\n"
"<Peter Gone> LA ?+1-121-544-8974 \n <R Steell> Quora Street AB-47209 +1-481-512-2222!\n"
"<Arthur Clarke> San Antonio $+1-121-504-8974 TT-45120\n <Ray Chandler> Teliman Pk. !+1-681-512-2222! AB-47209,\n"
"<Sophia Loren> +1-421-674-8974 Bern TP-46017\n <Peter O'Brien> High Street +1-908-512-2222; CC-47209\n"
"<Anastasia> +48-421-674-8974 Via Quirinal Roma\n <P Salinger> Main Street, +1-098-512-2222, Denver\n"
"<C Powel> *+19-421-674-8974 Chateau des Fosses Strasbourg F-68000\n <Bernard Deltheil> +1-498-512-2222; Mount Av.  Eldorado\n"
"+1-099-500-8000 <Peter Crush> Labrador Bd.\n +1-931-512-4855 <William Saurin> Bison Street CQ-23071\n"
"<P Salinge> Main Street, +1-098-512-2222, Denve\n")


# testing(phone(dr, "48-421-674-8974"), "Phone => 48-421-674-8974, Name => Anastasia, Address => Via Quirinal Roma")
# testing(phone(dr, "1-921-512-2222"), "Phone => 1-921-512-2222, Name => Wilfrid Stevens, Address => Wild Street AA-67209")
# testing(phone(dr, "1-908-512-2222"), "Phone => 1-908-512-2222, Name => Peter O'Brien, Address => High Street CC-47209")
# testing(phone(dr, "1-541-754-3010"), "Phone => 1-541-754-3010, Name => J Steeve, Address => 156 Alphand St.")
# testing(phone(dr, "1-121-504-8974"), "Phone => 1-121-504-8974, Name => Arthur Clarke, Address => San Antonio TT-45120")
# testing(phone(dr, "1-498-512-2222"), "Phone => 1-498-512-2222, Name => Bernard Deltheil, Address => Mount Av. Eldorado")
# testing(phone(dr, "1-098-512-2222"), "Error => Too many people: 1-098-512-2222")
# testing(phone(dr, "5-555-555-5555"), "Error => Not found: 5-555-555-5555")

str = '1-098-512-2222'

# print(phone(dr, str))
# __________________________________________________________________________________________________________________________________

"""Подсчитать число букв в строке малого регистра
при чем вывести только число букв выше 1"""

import re

def func(s: str):
    x = ''.join(re.findall(r'[a-z]',s))
    y = {i:x.count(i) for i in x.lower()}
    print(y)
    z = [f"{v}:{k*v}/" for k,v in y.items() if v > 1]
    z.sort(key=lambda x:x.split(':')[1],reverse=True)
    q = re.sub(r'\d','1',''.join(z))
    return (q)

s = "Sadus:cpms>orqn3zecwGvnznSgacs"
# s = 'codewars'
# s = "& aaa bbb c d"
# s = "A generation must confront the looming "
print(func(s))
# "1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr"

# {'h': 1, 'a': 4, 't': 3, 'c': 1,
#  'n': 2,'i': 1, 'd': 3, 'o': 5,
# 'y': 1, 'm': 1, 'r': 2, 'w': 1}

# ['4/: aaaa', '3/: ddd', '2/: nn',
# '5/: ooooo', '2/: rr', '3/: ttt']