import pyshorteners

s = pyshorteners.Shortener()
long_url = input('Paste your URL here')
short_url = s.tinyurl.short(long_url)
print(f"Shortened URL: {short_url}")
