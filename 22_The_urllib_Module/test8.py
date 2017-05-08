import urllib.robotparser


robot = urllib.robotparser.RobotFileParser()
# print(robot.set_url("http://arstechnica.com/robots.txt"))
# print(robot.read())
print(robot.can_fetch("*", "http://arstechnica.com/"))