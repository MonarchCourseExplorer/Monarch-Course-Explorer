import requests
from bs4 import BeautifulSoup
from course import Course

def scrapeCompSciCourses():
    url = "https://catalog.odu.edu/courses/cs/"
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find(id="undergraduatecoursestextcontainer")

    course_elements = results.find_all("div", class_="courseblock") #these are the individual courses blocks

    courses = []
    for element in course_elements:
        number = element.find("span", class_="detail-xrefcode").text
        title = element.find("span", class_="detail-title").text
        hours = element.find("span", class_="detail-hours_html").text
        detail = element.find("p", class_="courseblockextra").text
        prereqs = element.find("span", class_="detail-prereq")

        c = Course.parseCourse(number, title, hours, detail)
        courses.extend(c)

    for course in courses:
        course.printCourse()