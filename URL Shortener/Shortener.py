import pyshorteners

def shorten(url):
    s = pyshorteners.Shortener()
    short = s.tinyurl.short(url)
    return short

url = input("Enter the URL to shorten: ").strip()
try:
    short = shorten(url)
    print(f"Shortened URL: {short}")
except Exception as e:
    print(f"Error shortening URL: {e}")
