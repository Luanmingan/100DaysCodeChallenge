import pyperclip


AFFILIATE_CODE = '&tag=pyb0f-20'

url = pyperclip.paste()

if 'amazon' not in url:
    print('sorry, invalid link')
else:
    new_link = url + AFFILIATE_CODE
    pyperclip.copy(new_link)
    print('Affiliate link generated and copied to clipboard')
