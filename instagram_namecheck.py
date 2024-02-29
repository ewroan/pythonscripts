import sys
import requests

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
        'enc_password': '#PWD_INSTAGRAM_BROWSER%3A10%3A1709224787%3AAVRQACYLBMvTCSBF41HgxW6XunSqpohQ8vqcm021v6s0ok1Xe5VfAU518Y0WoGsGjqUANsaQC1MgBdRPeCViDraK2gdI3z8H4pfR4CRjhWqUi%2Bz3n%2BNyD6gTUI5Zu1fIaa9GpqGdsuuKz586bg%3D%3D',
        'email': 'deneme@deneme.com',
        'first_name': 'denemeci',
        'opt_into_one_tap': 'false',
        'username': username
    }

    response = requests.post(url, headers=headers, data=data)
    response_json = response.json()

    if response_json["dryrun_passed"] == True:
        print(f"The username '{username}' is available.")
    else:
        print(f"The username '{username}' is not available.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <username>")
        sys.exit(1)

    username = sys.argv[1]
    check_username(username)
