from qcloudsms_py import SmsMultiSender
from qcloudsms_py.httpclient import HTTPError

from tools.sms_config import appid, appkey, phone_numbers

sms_type = 0  # Enum{0: 普通短信, 1: 营销短信}
msender = SmsMultiSender(appid, appkey)
try:
    result = msender.send(sms_type, "86", phone_numbers,
                          "【腾讯云】您的验证码是: 5678", extend="", ext="")
except HTTPError as e:
    print(e)
except Exception as e:
    print(e)

print(result)
