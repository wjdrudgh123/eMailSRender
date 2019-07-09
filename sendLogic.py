import smtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import os
import tkinter.messagebox

#t = to, f = from, s = subject, m = text, p = path, word = pw, ts = ToServer, fs = 보내는 사람 메일 서버

def init_connection(t, f, s, m, p, word,ts, fs):
    smtp = smtplib.SMTP_SSL('smtp.naver.com', 465) #smpt 서버 연결 (SSL로 보안 연결)
    ToId = str(t)+"@"+ts
    FromId = str(f)+"@"+fs
    print(ToId)
    Pw = str(word)
    try:
        smtp.login(FromId, Pw)
        if p != '':
            msg = MIMEBase('multipart', 'mixed')
            
            cont = MIMEText(str(m), 'plain', 'utf-8')
            cont['Subject'] = str(s)

            msg.attach(cont)

            path = str(p)
            part = MIMEBase("application", "octet-stream")
            part.set_payload(open(path, 'rb').read())
            #인코딩
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment', filename=os.path.basename(path))
            msg.attach(part)

            smtp.sendmail(FromId, ToId, msg.as_string())
        else:
            msg = MIMEText(str(m), 'plain', 'utf-8')
            msg['Subject'] = str(s)
            smtp.sendmail(FromId, ToId, msg.as_string())
        tkinter.messagebox.showinfo("성공","메일을 성공적으로 보냈습니다.")
    except:
        tkinter.messagebox.showinfo("오류", "이메일이나 비밀번호 확인해보세요.")
    finally:
        smtp.quit()