from atproto import Client, client_utils
from secrets import secrets

def main():
	client = Client()

	username = secrets.get('BSKY_USER')
	password = secrets.get('BSKY_PASS')
	profile = client.login(username, password)
	print('Welcome,', profile.display_name)
	client.send_post(text="Hey, it's 9:11!")

if __name__ == '__main__':
	main()