from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

# SMTP 접속을 위한 서버, 계정 설정
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
# 보내는 메일 계정
SMTP_USER = "<your_gmail_address>"
SMTP_PASSWORD = "<your_google_app_password>"  # Google Email 앱비밀번호
# 참고: 구글 앱 비밀번호 생성 - https://support.google.com/accounts/answer/185833


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


# recipient_addr = 'stewart7@naver.com'
recipient_addr = 'stewart@daesung.com'
# recipient_addr = 'yugin.lim7@gmail.com'
subject = 'Python QLineEdit 숫자 입력 관련 Practices'
contents = 'Python QLineEdit에 숫자, 자릿수(최소/최대) 지정까지는 구현함. 그런데 천단위 콤마(,) 구현을 잘 모르겠음.'
# attached_file = '/home/kyungho/PythonProjects/Practices/영어단어-음식.ods'
attached_file = '//PyQt5_number.py'
# attached_file = '/home/kyungho/PythonProjects/Practices/email_sender.py'
send_mail(recipient_addr, subject, contents, attached_file)
