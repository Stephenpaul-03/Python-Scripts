import requests

def unshorten(url):
    try:
        response = requests.head(url, allow_redirects=True)
        return response.url
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None

short = input("Enter the shortened URL: ")
long = unshorten(short)
    
if long:
    print(f"The original URL is: {long}")
else:
    print("Could not unshorten the URL.")
