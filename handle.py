# -*- coding: utf-8 -*-#
# filename: handle.py
import hashlib
import reply
import receive
import web


class Handle(object):
    no = 0
    taken_id = []

    def __init__(self):
        print("init")

    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "token"  # 请按照公众平台官网\基本配置中信息填写

            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            map(sha1.update, list)
            hashcode = sha1.hexdigest()
            print("handle/GET func: hashcode, signature: ",
                    hashcode, signature)
            if hashcode == signature:
                return echostr
            else:
                return echostr
        except(Exception, Argument):
            return Argument 
    def POST(self):
        try:
            webData = web.data()
            print("Handle Post webdata is ", webData)
            #后台打日志
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
                content = str(recMsg.Content, 'utf-8')
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                print('content', content)
                if content == '抽奖':
                    print('user info', toUser, fromUser)
                    if toUser not in Handle.taken_id:
                        content = Handle.no
                        Handle.no = Handle.no + 1
                        replyMsg = reply.TextMsg(toUser, fromUser, content)
                        Handle.taken_id.append(toUser)
                        return replyMsg.send()
                    else:
                        content = "还想拿俩号?"
                        replyMsg = reply.TextMsg(toUser, fromUser, content)
                        return replyMsg.send()
                elif content == '情况':
                    content = Handle.no - 1
                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                    return replyMsg.send()
                else:
                    content = '请回复"抽奖"'
                    print('user info', toUser, fromUser)
                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                    return replyMsg.send()
            else:
                print("暂且不处理")
                return "success"
        except(Exception, Argment):
            return Argment
