import configparser
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

config = configparser.ConfigParser()
config.read('gmailconfig.ini')
smtp_user = config.get('gmail_app', 'smtp_user')
smtp_password = config.get('gmail_app', 'smtp_password')

"""
For generating google application password,
refer to the following : https://support.google.com/accounts/answer/185833
"""
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
SMTP_USER = smtp_user           # Google Mail Address
SMTP_PASSWORD = smtp_password   # Google Mail Application Password

# 이메일 유효성 검사 함수
def is_valid(addr):
    import re
    if re.match('(^[a-zA-Z-0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', addr):
        return True
    else:
        return False


# 이메일 보내기 함수
def send_mail(addr, subj_layout, cont_layout, attachment=None):
    if not is_valid(addr):
        print("Wrong email: " + addr)
        return

    # 텍스트 파일
    msg = MIMEMultipart("alternative")
    # 첨부파일이 있는 경우 mixed로 multipart 생성
    if attachment:
        msg = MIMEMultipart('mixed')
    msg["From"] = SMTP_USER
    msg["To"] = addr
    # 한 명에게 보낼 때
    # msg["To"] = "xxx@xxxxxxxx"
    # 여러 명에게 보낼 때(구분자는 콤마)
    # msg["To"] = "xxx@xxxxxxx, ooo@ooooooo"
    # 참조자
    # msg["Cc"] = "xxx@xxxxxxx"
    # 숨은참조(비밀참조)
    # msg["Bcc"] = "xxxx@xxxx, ooooo@ooooo"
    msg["Subject"] = subj_layout
    contents = cont_layout
    body = MIMEText(_text=contents, _charset="utf-8")
    # Html 형식의 본문 내용 (cid로 이미 첨부 파일을 링크했다.)
    # msg = MIMEText("Hello Test<br /><img src='cid:capture'>", 'html')
    msg.attach(body)
    # 첨부파일이 있으면
    if attachment:
        from email.mime.base import MIMEBase
        from email import encoders
        file_data = MIMEBase("application", "octect-stream")
        file_data.set_payload(open(attachment, "rb").read())
        encoders.encode_base64(file_data)
        import os
        filename = os.path.basename(attachment)
        file_data.add_header("Content-Disposition", 'attachment', filename=('UTF-8', '', filename))
        msg.attach(file_data)
    # smtp로 접속할 서버 정보를 가진 클래스변수 생성
    smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
    try:
        # 해당 서버로 로그인
        smtp.login(SMTP_USER, SMTP_PASSWORD)
        # 메일 발송
        smtp.sendmail(msg["From"], msg["To"], msg.as_string())
        # 여러명에게 보낼 때, 참조 추
        # smtp.sendmail(msg["From"], msg["To"].split(",")가 + msg["Cc"].split(","), msg.as_string())
    except Exception as e:
        print(e)
    finally:
        # 닫기 : smtp.quit()을 쓰는 것도 같다.
        smtp.close()


# recipient_addr = 'recipient address'
# subject = 'your subject'
# contents = 'email contents'
# # attached_file = 'None or your attachment file Path'
# attached_file = None
# send_mail(recipient_addr, subject, contents, attached_file)

recipient_addr = 'stewart7@naver.com'
subject = 'your subject'
contents = 'email contents'
# attached_file = 'None or your attachment file Path'
attached_file = None
send_mail(recipient_addr, subject, contents, attached_file)


