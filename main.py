from collections import defaultdict
import csv
import random
import time 
import smtplib, ssl
from email.mime.text import MIMEText


class RandomizeTasks:
    
    def __init__(self):
        self.names = {}
        self.task_list = ["Shlok", "Pandurangashtkam", "Aarti", "Reading", "Bhajan"]
        self.test_email_recipients = ["uchawada@gmail.com"]
        self.email_recipients = []
        self.file_name = "names_list.csv"

    def read_file(self):
        with open(self.file_name) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                self.names[row[0]] = row[1]

    def randomize(self):
        randomized_list = {}
        random_names = set()
        count = 0
        # get a random list of people (count of ) 
        while count< len(self.task_list):
            random_person = random.choice(list(self.names.keys()))
            if random_person in random_names:
                continue
            random_names.add(random_person)
            count = count + 1

        for i in range(0, len(random_names)):
            random_person = list(random_names)[i]
            randomized_list[random_person, self.names[random_person]] = self.task_list[i]
        
        return randomized_list

    def create_file(self, randomized_list):
        with open("randomized_file.txt", "w") as f:
            f.write("Name, Task\n")
            for k, v in randomized_list.items():
                f.write("{}, {}\n".format(k[0], v))

    def send_email(self):
        port = 587  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = "udchawada@gmail.com"
        receiver_email = "udchawada@gmail.com"
        password = "m$1204503504"
        message = "This is a test email"
        # Create a secure SSL context
        try:
            context = ssl.create_default_context()
            with smtplib.SMTP(smtp_server, port) as server:
                server.ehlo()
                server.starttls(context=context)
                server.ehlo()
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)
            print("Email sent!")
        except Exception as e:
            print("Unable to send email\nError: {}".format(e))

    def main(self):
        self.read_file()
        randomized_list = self.randomize()
        self.create_file(randomized_list)
        # self.send_file()
        self.send_email()


def main():
    a = RandomizeTasks()
    a.main()


if __name__ == "__main__":
    main()
 