# 阿里云短信验证码配置
SMS_CONFIG = {
    'ACCESS_KEY_ID': "LTAIDHOYSjYcvyVt",
    'ACCESS_KEY_SECRET': "qrEgykmXX4e6GUMFOqzuiLZ5gsUxSC",
    'SignName': "成少雷",
    'TemplateCode': "SMS_102315005"
}

# 短信应用 SDK AppID
appid = 1400009099  # SDK AppID 以1400开头
# 短信应用 SDK AppKey
appkey = "9ff91d87c2cd7cd0ea762f141975d1df37481d48700d70ac37470aefc60f9bad"
# 需要发送短信的手机号码
phone_numbers = ["13311259317", "15040913269", "15108461269"]
# 短信模板ID，需要在短信控制台中申请
template_id = 1400254355  # NOTE: 这里的模板 ID`7839`只是示例，真实的模板 ID 需要在短信控制台中申请
# 签名
sms_sign = "0f840377557888541b7ebec731688de0"  # NOTE: 签名参数使用的是`签名内容`，而不是`签名ID`。这里的签名"腾讯云"只是示例，真实的签名需要在短信控制台中申请
