def call():
    print('calling someone i dont know')
    return 'call done'

class Phone:
    price = 12000
    color = 'blue'
    brand = 'samsung'
    features = ['camera', 'speaker', 'hammer']

    def call(self):
        print(f'calling one person {self}')

    def send_sms(self, phone, sms):
        text = f'sending SMS to: {phone} and message: {sms}'
        return text 

my_phone = Phone()
my_phone.call()




