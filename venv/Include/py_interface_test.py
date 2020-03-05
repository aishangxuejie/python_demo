from suds.client import Client
import base64

# webservice url
url ="http://121.28.194.180:9020/his/ws/soap/sendHis?wsdl"
# 发起连接
clients1 = Client(url)
clients2 = Client(url)
str_encrypt = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><loginReqData><username>10000125</username><password>E10ADC3949BA59ABBE56E057F20F883E</password></loginReqData>"
str_leaveHos = "<?xml version=\"1.0\" encoding=\"utf-8\"?><leaveReqData><sessionid>57078</sessionid><akc190>10290113001</akc190><aac002>130123198310060080</aac002><aac003>王伟然</aac003><akc194>2018-12-08</akc194><akc195>1</akc195><akc196>F07.201</akc196><ints>22</ints><km05s><km05><aab034></aab034><aab301></aab301><aac002>130203194208262411</aac002><aac003>王伟然</aac003><aac004>男</aac004><aac005>汉族</aac005><aac006>1942-08-26</aac006><aac009></aac009><aac010>河北省唐山市</aac010><aac020>工人</aac020><aac021>已婚</aac021><aad005></aad005><aad007></aad007><aad010>唐钢二钢</aad010><aae005></aae005><aae006></aae006><aae007></aae007><aae010>福乐园812-4-302</aae010><aae017>063000</aae017><aam003>王会兰</aam003><aam005>15033341055</aam005><aam010>福乐园812-4-302</aam010><aam036>亲属</aam036><akc020>中国</akc020><akc023></akc023><akc192>2019-02-15</akc192><akc194></akc194><alc028></alc028><alc029></alc029><alc030></alc030><blm001></blm001><blm002>14</blm002><blm003>116656*14</blm003><blm004></blm004><blm005>神经内科二病区</blm005><blm006></blm006><blm007></blm007><blm009></blm009><blm010></blm010><blm011>0</blm011><blm012></blm012><blm013></blm013><blm014></blm014><blm015></blm015><blm016></blm016><blm017>未做</blm017><blm018>未做</blm018><blm019>未查</blm019><blm020></blm020><blm021></blm021><blm022>许斌</blm022><blm023>许斌</blm023><blm024>郭瑶</blm024><blm025></blm025><blm026></blm026><blm027></blm027><blm028>丙</blm028><blm029></blm029><blm030></blm030><blm031></blm031><blm032></blm032><blm033></blm033><blm034></blm034><blm035></blm035><blm036></blm036><blm037></blm037><blm038></blm038><blm039></blm039><blm040>否</blm040><blm041></blm041><blm042>否</blm042><blm043></blm043><blz068>待定其他方面未指</blz068></km05></km05s></leaveReqData>"


# print(str_encrypt)
base64_encrypt = base64.b64encode(str_encrypt.encode('utf-8'))
base64_leaveHos = base64.b64encode(str_leaveHos.encode('utf-8'))

#print(clients)   # 输出返回信息，可以获知有那些method可以调用
#字符串被b''包围了 b 表示 byte 将编码后的再转换回去
inputs = input("请输入：")
res1 =""
res2 =""
if ( inputs == "0"):
	res1 = clients1.service.leaveHos(str(base64_leaveHos,'utf-8'))
	res2 = clients2.service.leaveHos(str(base64_leaveHos,'utf-8'))
else:
	res1 = clients1.service.login(str(base64_encrypt,'utf-8'))

base64_decrypt1 = base64.b64decode(res1.encode('utf-8'))
base64_decrypt2 = base64.b64decode(res2.encode('utf-8'))
# print("入参：")
# print(logout)
print("出参：")
print(str(base64_decrypt1,'utf-8'))   # 打印返回信息
print(str(base64_decrypt2,'utf-8'))   # 打印返回信息