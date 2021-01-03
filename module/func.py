from django.conf import settings

from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage, StickerSendMessage, LocationSendMessage, QuickReply, QuickReplyButton, MessageAction

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

def goodnight(event):  #傳送文字
    try:
        message = [  #串列
            TextSendMessage(  
                text = "別擔心我準備要洗洗睡了!媽媽晚安~:D"
            ),  
            StickerSendMessage(  #傳送貼圖
                package_id='2',  
                sticker_id='26'
            ),
        ]  
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sleepearly(event):  #傳送文字
    try:
        message = [  #串列
            TextSendMessage(  
                text = "我最近都很早睡喔"
            ),  
            TextSendMessage(  
                text = "我都有照顧好自己~放心!"
            ),
        ]  
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))        

def dowhat(event):  #多項傳送
    try:
        message = [  #串列
            TextSendMessage(  #傳送y文字
                text = "我們在學校佈展"
            ),
            TextSendMessage(  
                text = "放心吧不會太晚!"
            ),           
            ImageSendMessage(  #傳送圖片
                original_content_url = "https://i.imgur.com/KqvXDA2.jpg",
                preview_image_url = "https://i.imgur.com/KqvXDA2.jpg"
            )
        ]
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

#def sendImage(event):  #傳送圖片
 #   try:
  #      message = ImageSendMessage(
   #         original_content_url = "https://i.imgur.com/4QfKuz1.png",
    #        preview_image_url = "https://i.imgur.com/4QfKuz1.png"
     #   )
      #  line_bot_api.reply_message(event.reply_token,message)
    #except:
     #   line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

#def sendStick(event):  #傳送貼圖
 #   try:
  #      message = StickerSendMessage(  #貼圖兩個id需查表
   #         package_id='1',  
    #        sticker_id='2'
     #   )
      #  line_bot_api.reply_message(event.reply_token, message)
#    except:
 #       line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

#def sendMulti(event):  #多項傳送
 #   try:
 #       message = [  #串列
  #          StickerSendMessage(  #傳送貼圖
 #               package_id='1',  
  #              sticker_id='2'
   #         ),
    #        TextSendMessage(  #傳送y文字
      #          text = "這是 Pizza 圖片！"
     #       ),
       #     ImageSendMessage(  #傳送圖片
        #        original_content_url = "https://i.imgur.com/4QfKuz1.png",
         #       preview_image_url = "https://i.imgur.com/4QfKuz1.png"
          #  )
        #]
        #line_bot_api.reply_message(event.reply_token,message)
 #   except:
  #      line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
