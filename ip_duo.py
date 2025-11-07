import requests
from bs4 import BeautifulSoup

def get_ip_info(ip):
    print(f"\n📡 Информация об IP {ip} (ipinfo.io):")
    try:
        r = requests.get(f"https://ipinfo.io/{ip}/json")
        r.raise_for_status()
        data = r.json()
        for k, v in data.items():
            print(f"{k:15}: {v}")
    except Exception as e:
        print(f"Ошибка при запросе ipinfo.io: {e}")

def check_abuseipdb(ip, api_key):
    print(f"\n🚨 Проверка IP {ip} на abuseipdb.com:")
    url = "https://api.abuseipdb.com/api/v2/check"
    headers = {
        'Key': api_key,
        'Accept': 'application/json'
    }
    params = {
        'ipAddress': ip,
        'maxAgeInDays': 90
    }
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()['data']
        print(f"IP: {data['ipAddress']}")
        print(f"Уровень угрозы: {data['abuseConfidenceScore']}%")
        print(f"Тип использования: {data.get('usageType', 'Не указано')}")
        print(f"Страна: {data.get('countryCode', '??')}")
        print(f"Последний репорт: {data.get('lastReportedAt', 'не было')}")
    except Exception as e:
        print(f"Ошибка при запросе abuseipdb: {e}")

def search_duckduckgo(ip):
    print(f"\n🔍 Поиск утечек на dehashed.com через DuckDuckGo по IP {ip}:")
    query = f'"{ip}" site:dehashed.com'
    url = f"https://html.duckduckgo.com/html/?q={query}"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        links = soup.find_all("a", class_="result__a")
        if links:
            for link in links:
                print("🔗", link.get("href"))
        else:
            print("❌ Утечек на dehashed.com не найдено.")
    except Exception as e:
        print(f"Ошибка при поиске в DuckDuckGo: {e}")

if __name__ == "__main__":
    ip = input("Введите IP-адрес для OSINT-анализа: ").strip()
    abuse_api_key = "887d5160ab27a7f6c65b8f1ada46c27a6a6edf46993ce01d40182e0da1f7542c92c6627371acf9e4".strip()

    get_ip_info(ip)
    check_abuseipdb(ip, abuse_api_key)
    search_duckduckgo(ip)
