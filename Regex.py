import re

myStr = "Tata Consultancy Services att Limited is an Indian multinational information technology services and " \
        "consulting company headquartered in Mumbai, Maharashtra, India. It is a subsidiary of the Tata Group and " \
        "operates in 149 locations across 46 countries. TCS is the second largest Indian company by market " \
        "capitalisation "

"""
findall, search, split, sub, finditer
"""
# patt = re.compile(r'company')
# patt = re.compile(r'.')  # any character (except newline character)
# patt = re.compile(r'^Tata')  # starts withs
# patt = re.compile(r'tion$')  # end withs
# patt = re.compile(r'at*')  # zero or more occurrences
# patt = re.compile(r'at+')  # one or more occurrences
# patt = re.compile(r'at{2}')  # exactly the specified no of occurrences
# patt = re.compile(r'(ta)')  # capture and group
# patt = re.compile(r'at|an')  # Either or

# Special sequence

patt = re.compile(r'\bTata')
matches = patt.finditer(myStr)
for match in matches:
    print(match)
print(myStr[108:115])
