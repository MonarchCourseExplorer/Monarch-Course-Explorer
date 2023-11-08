import re

class Course:

    def __init__(self):
        pass
    
    def parseCourse(number, title, hours, detail):
        #a single block can represent 2 courses - a 400 and 500 level course
        #for now splitting them, but there should be a way to reference back beyond the last 2 numbers?

        numbers = re.findall(r'\d+', number)
        department = number.split()[0]
        
        if len(numbers) == 1:
            c = Course()
            c.department = department
            c.number = numbers[0]
            c.title = title

            #parse hours, options are 3 or 1-3
            allHours = re.findall(r'\d+', hours)
            minHours = allHours[0]
            if len(allHours) > 1:
                maxHours = allHours[1]
                c.credits = minHours + "-" + maxHours
            else:
                maxHours = None
                c.credits = minHours

            c.detail = detail

            return [c]
        else:
            return map(lambda n: Course.parseCourse(department + ' ' + n, title, hours, detail)[0], numbers)

    def printCourse(self):
        print("{1} {0}".format(self.number, self.department))
        print(self.title)

        print("Credit hours: {0}".format(self.credits))
            
        print(self.detail)
        print()