# making a birthday wish with the help of smtp protocol
import smtplib
my_email = "srinadhkonduri@gmail.com"
password = "12345"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="srinadhkonduri2003@gmail.com", msg="hello")
connection.close()
