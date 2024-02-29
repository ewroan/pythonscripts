import sys
import requests
import json

def check_username(username):
    url = 'https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/'
    headers = {
        'authority': 'www.instagram.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,tr;q=0.8,ko;q=0.7,la;q=0.6',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'csrftoken=XFmraqYmB5jP7-JthZB5t1; ps_l=0; ps_n=0; ig_did=C338771C-B95D-428D-9A44-FFE70B6DB3BD; datr=yxTGZW56pyhmkK1E64L2DNgw; ig_nrcb=1; mid=ZcYUzAAEAAFf_5z-3_hqpunn_HiR',
        'dpr': '2',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/accounts/emailsignup/',
        'sec-ch-prefers-color-scheme': 'dark',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'sec-ch-ua-full-version-list': '"Chromium";v="122.0.6261.69", "Not(A:Brand";v="24.0.0.0", "Google Chrome";v="122.0.6261.69"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"macOS"',
        'sec-ch-ua-platform-version': '"14.3.1"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'viewport-width': '1055',
        'x-asbd-id': '129477',
        'x-csrftoken': 'XFmraqYmB5jP7-JthZB5t1',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': '0',
        'x-instagram-ajax': '1011741444',
        'x-requested-with': 'XMLHttpRequest'
    }

    data = {
        'enc_password': '#PWD_INSTAGRAM_BROWSER:10:1709226660:AVRQADdBH2oBueJyfjjShzG381RzvQSZYZlgLzJ8FGnp+5c/xPqaDL1mhQgI5cC1Rv/k82EN2/xIwnVYJhyIWaPaBc2B/XOLxw1aYJD1171bFDK6S9GYoheQmJa/J3u2RC6BrxvpSzAzTVMFk1Q=',
        'email': 'u@namecheckpythonforexample.com',
        'first_name': 'namecheckpythonforexample',
        'username': username,
        'opt_into_one_tap': 'false'
    }

    response = requests.post(url, headers=headers, data=data)
    response_json = response.json()

    #json_formatted_str = json.dumps(response_json, indent=2)
    #print(json_formatted_str)
    #print(response_json["dryrun_passed"])

    if response_json.get('dryrun_passed', True):
        print(f"The username '{username}' is AVAILABLE")
    else:
        print(f"The username '{username}' is NOT available")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script.py <username>")
        sys.exit(1)

    username = sys.argv[1]
    check_username(username)
