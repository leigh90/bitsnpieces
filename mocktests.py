
from urllib.parse import parse_qs, urlparse

parsed_url = urlparse('https://www.youtube.com/watch?v=LzK2rviPo4c&ab_channel=CNBC')
second_url = urlparse("https://www.jw.org/en/search/?q=how+to+be+a+good+dad&link=%2Fresults%2FE%2Fall%3Fq%3D")
this = parse_qs(parsed_url.query)
that = parse_qs(second_url.query)

print(this)
print(that)

print(type(this))
