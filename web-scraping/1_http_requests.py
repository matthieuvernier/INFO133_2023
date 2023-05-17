from requests_html import HTMLSession

session = HTMLSession()

print("1-----------POST---------")
response = session.post('http://httpbin.org/post', data="Hola")
print(response.request.url)
print(response.request.headers)
print(response.request.body)
print(response.status_code)


print("2-----------GET---------")
response = session.get('http://httpbin.org/get')
print(response.request.url)
print(response.request.headers)
print(response.request.body)
print(response.status_code)
