import requests

url = 'https://steamdb.info/sales/'
apikey = 'a758dc1f189810e5297759570a56ed5f29533468'
params = {
    'url': url,
    'apikey': apikey,
    'js_render': 'true',
    'antibot': 'true',
    'js_instructions': """[{"click":".selector"},{"wait":500},{"fill":[".input","value"]},{"wait_for":".slow_selector"}]""",
    'premium_proxy': 'true',
}
response = requests.get('https://api.zenrows.com/v1/', params=params)

if response.status_code == 200:
    data_site = response.text
else:
    raise Exception("Erro na requisição", response.status_code, response.text)
