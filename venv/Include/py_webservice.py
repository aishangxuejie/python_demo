from suds.client import Client
import base64

# webservice url
url ="http://121.28.194.180:9020/his/ws/soap/sendHis?wsdl"
# url ="http://www.sunreal.cn:8023/hbhis/ws/soap/sendHis?wsdl"
# 发起连接
clients = Client(url)

str_encrypt = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><loginReqData><username>10000125</username><password>E10ADC3949BA59ABBE56E057F20F883E</password></loginReqData>"
logout = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><logoutReqData><sessionid>58351</sessionid><username>10000125</username><password>1637F44C03AE028FEDCA295E8DD371C9</password></logoutReqData>"
getDevice = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><getDeviceReqData><sessionid>58351</sessionid><aac001>378713</aac001><alca02></alca02><akc176start>2019-04-01</akc176start><akc176end/></getDeviceReqData>"
sendDevice = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><sendDeviceReqData><sessionid>58351</sessionid><kc21><akc190>fzqj201905</akc190><alca02>201604023628</alca02><aab001>13040120187</aab001><aac001>1360010307013</aac001><aac004>1</aac004><aka130>90</aka130><akc191>5</akc191><akc192>2019-04-05</akc192></kc21><meds><med><alc400>666</alc400><alc401>2019-04-05</alc401><alc402>11</alc402><alc403>大腿假肢</alc403><alc405>22000.00</alc405><alc406>1</alc406><alc407>22000.00</alc407><akc230>PP医用承筒、合金四轴气压膝关节、动踝</akc230></med></meds></sendDeviceReqData>"
revokeDevice = "<?xml version=\"1.0\" encoding=\"utf-8\"?><revokeDeviceReqData><sessionid>58351</sessionid><akc190>fzqj1231112122</akc190></revokeDeviceReqData>"
getAuditReqData = "<?xml version=\"1.0\" encoding=\"utf-8\"?><auditReqData><sessionid>58351</sessionid><akc190>fzqj1231112122</akc190><aae002></aae002></auditReqData>"
getPerDevice = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><perDetailReqData><sessionid>58351</sessionid><aae036s/><aae036e/><akc190/><aac002/><aac003/></perDetailReqData>"

# print(str_encrypt)
base64_encrypt = base64.b64encode(str_encrypt.encode('utf-8'))
base64_logout = base64.b64encode(logout.encode('utf-8'))
base64_getDevice = base64.b64encode(getDevice.encode('utf-8'))
base64_sendDevice = base64.b64encode(sendDevice.encode('utf-8'))
base64_revokeDevice = base64.b64encode(revokeDevice.encode('utf-8'))
base64_getAuditReqData = base64.b64encode(getAuditReqData.encode('utf-8'))
base64_getPerDevice = base64.b64encode(getPerDevice.encode('utf-8'))

#print(clients)   # 输出返回信息，可以获知有那些method可以调用
#字符串被b''包围了 b 表示 byte 将编码后的再转换回去
inputs = input("请输入：")
if ( inputs == "0"):
	res = clients.service.getDeviceDetails(str(base64_getDevice,'utf-8'))
elif ( inputs == "1"):
	res = clients.service.sendDeviceDetails(str(base64_sendDevice,'utf-8'))
elif (inputs == "2"):
	res = clients.service.revokeDeviceDetails(str(base64_revokeDevice,'utf-8'))
elif (inputs == "3"):
	res = clients.service.getDeviceDetailsAudit(str(base64_getAuditReqData,'utf-8'))
elif (inputs == "4"):
	res = clients.service.getPerDeviceDetail(str(base64_getPerDevice,'utf-8'))
else:
	res = clients.service.login(str(base64_encrypt,'utf-8'))

base64_decrypt = base64.b64decode(res.encode('utf-8'))
# print("入参：")
# print(logout)
print("出参：")
print(str(base64_decrypt,'utf-8'))   # 打印返回信息

# 接下去可以解析这些返回信息(res)，获取我们需要的数据了