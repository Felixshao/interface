import yagmail
import time
from config.readConfig import ReadConfig

emall = ReadConfig()
on_off = emall.get_emall('on_off')   # 开关
subject = emall.get_emall('subject')     # 标题
smtp = emall.get_emall('smtp')      # 邮箱服务器
emall_user = emall.get_emall('emall_user')  # 邮箱账号
emall_pass =  emall.get_emall('emall_pass')     # 邮箱密码
emall_to = emall.get_emall('emall_to')      # 接收者邮箱


class operate_emall():

    def send_emall(self, file_name=None):

        em = yagmail.SMTP(user=emall_user, password=emall_pass, host=smtp)
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        content = '接口自动化报告！！！'
        em.send(to=emall_to, subject=subject+current_time, contents=content, attachments=file_name)


if __name__ == '__main__':

    operate_emall().send_emall()
