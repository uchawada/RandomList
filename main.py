from collections import defaultdict
import csv

class RandomizeTasks:
    
    def __init__(self):
        self.names = defaultdict()

    def read_file(self):
        with open('names_list.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                self.names[row[0]] = row[1]
        for k, v in self.names.items():
            print(k,v)

    def randomize(self):
        print("randomize")

    def send_file(self):
        print("send file")
    
    def main(self):
        self.read_file()


def main():
    a = RandomizeTasks()
    a.main()


if __name__ == "__main__":
    main()
 