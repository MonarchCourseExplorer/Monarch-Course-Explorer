import re

class Course:
    
    def parseCourse(self, number, title, hours, detail):
        self.number = number
        self.title = title

        #parse hours, options are 3 or 1-3
        allHours = re.findall(r'\d+', hours)
        self.minHours = allHours[0]
        if len(allHours) > 1:
            self.maxHours = allHours[1]
        else:
            self.maxHours = None

        self.detail = detail

    def printCourse(self):
        print(self.number)
        print(self.title)

        if self.maxHours == None:
            print("Credit hours: {0}".format(self.minHours))
        else:
            print("Credit hours: {0}-{1}".format(self.minHours, self.maxHours))
            
        print(self.detail)
        print()