from instagrapi import Client
from itertools import cycle
import time

def login_instagram(username, password, proxy):
    """
    Logs into Instagram and returns an authenticated Client instance.
    Handles challenges like CAPTCHA and 2FA.
    """
    cl = Client()
    cl.set_proxy(proxy)
    try:
        cl.login(username, password)
    except Exception as e:
        print(f"Initial login failed: {e}")
        challenge_resolve(cl)
    return cl

def challenge_resolve(cl):
    """
    Resolves Instagram challenges like CAPTCHA or 2FA.
    """
    try:
        challenge_choice = cl.challenge_resolve_simple(choice='email')
        if challenge_choice:
            code = input("Enter the code sent to your email: ")
            cl.challenge_send_code(code)
    except Exception as e:
        print(f"Challenge resolution failed: {e}")

def fetch_business_profiles(cl, category, country):
    """
    Fetches business profiles based on a category and country.
    """
    hashtag = cl.hashtag_info(category)
    posts = cl.hashtag_medias_recent(hashtag.name, amount=50)  # Fetch recent 50 posts

    # Filter posts by country (this assumes location data is available in posts)
    profiles = []
    for post in posts:
        if post.location and country.lower() in post.location.name.lower():
            profiles.append(post.user.username)
    
    return profiles

def main(username, password, proxies, category, country):
    proxy_pool = cycle(proxies)
    cl = None
    while cl is None:
        proxy = next(proxy_pool)
        try:
            cl = login_instagram(username, password, proxy)
            print(f"Logged in with proxy {proxy}")
        except Exception as e:
            print(f"Proxy {proxy} failed: {e}")
            cl = None
            time.sleep(60)  # Wait a bit before trying the next proxy

    profiles = fetch_business_profiles(cl, category, country)
    print(f"Business profiles in {category} category from {country}:")
    for profile in profiles:
        print(profile)

if __name__ == "__main__":
    username = "ryan_kyrillos"
    password = "Kyrillos1234_rayenig"
    
    # List of proxies to cycle through
    proxies = [
        "http://20.219.176.57:3129",
    "http://89.145.162.81:3128",
    "http://20.235.159.154:80",
    "http://188.209.49.99:80",
    "http://154.16.146.46:80",
    "http://50.62.183.223:80",
    "http://5.196.65.71:3128",
    "http://72.10.164.178:4015",
    "http://62.33.53.248:3128",
    "http://91.189.177.189:3128",
    "socks4://47.76.144.139:4006",
    "http://39.125.131.121:80",
    "http://91.189.177.186:3128",
    "http://152.26.229.86:9443",
    "http://93.103.221.133:80",
    "http://116.63.129.202:6000",
    "http://206.189.12.206:80",
    "http://45.9.75.76:4444",
    "http://72.10.164.178:15529",
    "socks4://72.217.216.239:4145",
    "socks4://185.210.227.102:4145",
    "http://72.10.160.171:17485",
    "http://95.164.113.107:80",
    "http://72.10.164.178:8979",
    "http://72.10.160.174:19153",
    "http://72.10.164.178:3653",
    "http://80.249.112.162:80",
    "http://67.43.228.252:18391",
    "http://37.27.82.72:80",
    "http://64.227.4.244:8888",
    "http://67.43.227.227:2433",
    "http://161.34.40.32:3128",
    "socks4://203.77.237.62:4153",
    "http://154.16.146.41:80",
    "socks4://178.176.134.67:3629",
    "http://89.35.237.187:8080",
    "http://141.148.26.234:8081",
    "http://114.156.77.107:8080",
    "http://103.153.154.6:80",
    "http://95.216.140.215:80",
    "http://89.35.237.187:8888",
    "http://154.203.132.49:8090",
    "http://72.10.164.178:29285",
    "socks4://199.116.114.11:4145",
    "http://67.43.227.227:20675",
    "http://72.10.160.174:14825",
    "http://49.13.252.196:80",
    "http://148.251.248.244:80",
    "socks4://85.117.56.146:4145",
    "http://89.35.237.187:4153",
    "http://212.107.28.120:80",
    "http://90.84.17.133:3128",
    "http://51.15.242.202:8888",
    "http://85.214.107.177:80",
    "http://13.80.177.101:8118",
    "http://152.26.229.88:9443",
    "http://47.89.184.18:3128",
    "socks4://24.75.156.114:3366",
    "http://189.240.60.171:9090",
    "http://62.72.29.174:80",
    "socks4://51.161.131.84:62969",
    "socks4://45.15.170.94:32768",
    "http://83.98.243.181:80",
    "http://84.252.73.132:4444",
    "http://89.35.237.187:4145",
    "http://72.10.160.90:10747",
    "socks4://124.158.153.33:1080",
    "socks4://216.152.219.108:30400",
    "http://67.43.236.20:22499",
    "http://185.105.90.88:4444",
    "http://154.16.146.43:80",
    "http://152.26.229.57:9443",
    "http://203.19.38.114:1080",
    "socks4://138.36.150.27:1080",
    "socks4://184.178.172.25:15291",
    "http://119.9.77.49:8080",
    "http://58.246.58.150:9002",
    "http://103.49.202.252:80",
    "socks4://47.237.2.245:8080",
    "http://34.81.72.31:80",
    "http://223.85.12.114:2222",
    "socks4://101.34.7.205:1080",
    "socks4://146.59.70.29:13513",
    "http://36.94.30.238:8080",
    "http://5.78.118.7:10000",
    "http://159.54.149.67:80",
    "socks4://198.12.253.239:15932",
    "http://67.43.227.227:21413",
    "http://67.43.227.227:28359",
    "http://85.209.153.174:80",
    "http://180.250.161.42:80",
    "http://67.43.227.227:25295",
    "http://185.217.198.121:4444",
    "http://72.10.164.178:4145",
    "http://85.209.153.175:3128",
    "http://72.10.164.178:18627",
    "http://85.209.153.173:999",
    "http://83.169.17.201:80",
    "http://43.255.113.232:8080",
    "http://85.209.153.174:4153",
    "http://4.236.183.37:8080",
    "http://125.77.25.178:8090",
    "http://47.91.65.23:3128",
    "http://182.16.187.212:8080",
    "http://185.232.169.108:4444",
    "socks4://103.12.246.33:4145",
    "socks5://8.213.222.247:9080",
    "http://176.32.2.193:8080",
    "http://159.69.86.130:80",
    "http://197.248.75.221:8104",
    "http://94.130.94.45:80",
    "http://200.39.120.123:999",
    "http://37.52.15.70:8080",
    "http://103.172.42.237:8080",
    "http://83.68.136.236:80",
    "http://72.10.160.90:24907",
    "http://82.200.237.11:8080",
    "http://103.172.70.27:1111",
    "http://45.117.29.33:58080",
    "http://154.16.146.45:80",
    "http://154.16.146.48:80",
    ]
    
    category = "restaurant"  # Example category
    country = "USA"          # Example country

    main(username, password, proxies, category, country)
