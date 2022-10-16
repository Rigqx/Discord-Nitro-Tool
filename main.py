import threading, requests, string, json, random, time, socket, os
from colorama import Fore, Back, Style

class Nitro:
	def generateCodes(amout):
		for i in range(amout):
			code = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
			print(code)
			with open("./output/codes.txt", 'a', encoding='UTF-8') as file:
				file.write(code + "\n")
				file.close()
			time.sleep(0.1)

	def checkCode():
		with open("./input/proxies.txt", encoding="utf-8") as f:
			proxies = [i.strip() for i in f]

		working = 0
		notworking = 0

		with open("./output/codes.txt", 'r', encoding='UTF-8') as file:
			while (line := file.readline().rstrip()):
				proxy = random.choice(proxies)

				os.system(f'title Nitro Checker - {working}/{notworking}')
				
				r = requests.post(f"https://discordapp.com/api/v9/entitlements/gift-codes/{line}?with_application=false&with_subscription_plan=true", proxies={"https": "http" + "://" + proxy})
				if r.status_code == 200:
					print(Fore.GREEN + f"  [+] {line} - {proxy}")
					working += 1
				else:
					notworking += 1
				
if __name__ == "__main__":
	Nitro.checkCode()