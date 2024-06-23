#say gex
import sys
import re

uwu_dict = {
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
    "onegai": "open"
}

def twanswataw(content):
    pattern = re.compile(r'\b(' + '|'.join(re.escape(key) for key in uwu_dict.keys()) + r')\b')
    return pattern.sub(lambda x: uwu_dict[x.group()], content)
def oniisaaaaan(pathywathy):
    with open(pathywathy, 'r', encoding='utf-8') as file:
        uwubutrealtime = file.read()
    stinkycode = twanswataw(uwubutrealtime)
    exec(stinkycode, globals())
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uwusage: python uwuthon.py <script.uwu>")
    else:
        oniisaaaaan(sys.argv[1])
