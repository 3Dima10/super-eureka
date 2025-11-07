import requests

def get_ip_info(ip):
    print(f"\n📡 [1] Информация об IP {ip} через ipinfo.io")
    r = requests.get(f"https://ipinfo.io/{ip}/json")
    if r.status_code == 200:
        data = r.json()
        for k, v in data.items():
            print(f"{k:15}: {v}")
    else:
        print("Ошибка при запросе ipinfo.io")

def check_abuseipdb(ip, api_key):
    print(f"\n🚨 [2] Проверка на спам и злоупотребления через AbuseIPDB")
    url = "https://api.abuseipdb.com/api/v2/check"
    headers = {
        'Key': api_key,
        'Accept': 'application/json'
    }
    params = {
        'ipAddress': ip,
        'maxAgeInDays': 90
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()['data']
        print(f"IP: {data['ipAddress']}")
        print(f"Уровень угрозы: {data['abuseConfidenceScore']}%")
        print(f"Типы злоупотреблений: {data.get('usageType', 'Не указано')}")
        print(f"Страна: {data.get('countryCode', '??')}")
        print(f"Последнее сообщение об активности: {data.get('lastReportedAt', 'не было')}")
    else:
        print("Ошибка при запросе в AbuseIPDB")

if __name__ == "__main__":
    ip = input("Введите IP для анализа: ").strip()
    abuse_api_key = "887d5160ab27a7f6c65b8f1ada46c27a6a6edf46993ce01d40182e0da1f7542c92c6627371acf9e4".strip()
    
    get_ip_info(ip)
    check_abuseipdb(ip, abuse_api_key)
