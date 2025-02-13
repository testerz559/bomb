import requests
purple = "\033[1;35m"
violet_chu = "\033[1;35m"
darkblue = "\033[34m"
green = "\033[1;32m"
red = "\033[1;31m"
yellow = "\033[1;33m"
skyblue = "\033[1;36m"
blue = "\033[1;34m"
lightblue = "\033[38;5;81m"
hotpink = "\033[38;5;197m"
light_magenta = "\033[38;5;174m"
white = "\033[1;37m"
lavender = "\033[38;5;189m"
rasp = "\033[38;5;22m"
darkblue = "\033[34m"
green = "\033[1;32m"
red = "\033[1;31m"
yellow = "\033[1;33m"
skyblue = "\033[1;36m"
blue = "\033[1;34m"
lightblue = "\033[38;5;81m"
white = "\033[1;37m"
def banner():


    print(f"""{red}
███████╗███╗   ███╗███████╗    ██████╗  ██████╗ ███╗   ███╗██████╗ ███████╗██████╗ 
██╔════╝████╗ ████║██╔════╝    ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██╔════╝██╔══██╗
███████╗██╔████╔██║███████╗    ██████╔╝██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
╚════██║██║╚██╔╝██║╚════██║    ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
███████║██║ ╚═╝ ██║███████║    ██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
╚══════╝╚═╝     ╚═╝╚══════╝    ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝

                        Created & Manipulated by : Jovan / D3ATH                                        
""")
    print("     \033[1;34m───────────────────────────────────────────────────────────────\033[0m")
def send_spam_sms():
    banner()
    print()
    phone = input(f"{green}Enter the phone number: ")
    print("     \033[1;34m───────────────────────────────────────────────────────────────\033[0m")
    count = input(f"{green}Enter the number of messages to send: ")
    print("     \033[1;34m───────────────────────────────────────────────────────────────\033[0m")
    interval = input(f"{green}Enter the interval (in seconds): ")
    
    url = f"https://kaiz-apis.gleeze.com/api/spamsms?phone={phone}&count={count}&interval={interval}"
    

    
    try:
        response = requests.get(url)  # First, try GET request
        if response.status_code == 404:
            print("GET request failed. Trying POST request...")
            response = requests.post(url)  # If GET fails, try POST
        
        print(f"Response Code: {response.status_code}")
        print(f"Response Text: {response.text}")
        
        if response.status_code == 200:
            try:
                data = response.json()
                print(f"Status: {data.get('status', 'unknown')}")
                print(f"Message: {data.get('message', 'No message provided')}")
            except ValueError:
                print("Failed to parse JSON response.")
        else:
            print("Failed to send request. Check API URL and parameters.")
    except requests.RequestException as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    send_spam_sms()
