import re
mapping = {
    "impowt": "import",
    "wetuwn": "return",
    "nyot": "not",
    "wif": "with",
    "owos": "os",
    "jsnyan": "json",
    "pwint": "print",
    "pwenetwate": "write",
    "eh": "if",
    "mwakediws": "makedirs",
    "length_OwO": "range",  
    "ree": "re",
    "GiveMeAttentionSenpai": "response",
    "weqwests": "requests",
    "rub": "get",
    "open": "onegai"
}

def twanswatetwouwu(code):
    lines = code.split('\n')
    twanswated_lines = []

    for line in lines:
        for key, value in mapping.items():
            line = re.sub(r'\b' + re.escape(value) + r'\b', key, line)
        twanswated_lines.append(line)    
    return '\n'.join(twanswated_lines)

def fixmesenpai(pywopath, uwupathywathy):
    with open(pywopath, 'r', encoding='utf-8') as file:
        codywody = file.read()

    uwu_code = twanswatetwouwu(codywody)

    with open(uwupathywathy, 'w', encoding='utf-8') as file:
        file.write(uwu_code)

pywopath = 'script.py'
uwupathywathy = 'script.uwu'
fixmesenpai(pywopath, uwupathywathy)