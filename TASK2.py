"""
Authentication GitHub API https://docs.github.com/en/rest?apiVersion=2022-11-28 for OAuth 2.0 authentication
Task: Create a Postman collection for GitHub OAuth authentication and data access. Then write a python script to
automate this authentication process (use requests-oauthlib)
"""
from requests_oauthlib import OAuth2Session


client_id = '07550889a7cf7c2923a6'
client_secret = 'b441911cfb9c3c0044c9f98af74ff2510bbff6d7'
redirect_uri = 'https://localhost:3000/callback'
scope = ['repo']


oauth2_session = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=scope)


authorization_url, state = oauth2_session.authorization_url('https://github.com/login/oauth/authorize')


print("Visit this URL to authenticate: ")
print(authorization_url)


authorization_code = input("Enter the authorization code from the URL: ")
token = oauth2_session.fetch_token('https://github.com/login/oauth/access_token', code=authorization_code, client_secret=client_secret)


response = oauth2_session.get('https://api.github.com/user/repos')
print("GitHub User Info:")
print(response.json())
