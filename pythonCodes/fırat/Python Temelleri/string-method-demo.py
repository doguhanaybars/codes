website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

txt = " Hello World "

# print(txt.strip())
result = website.lstrip("/:pths")
result = "www.sadikturan.com".strip("w.moc")
result = course.casefold()
result = website.count("a")
result = website.find("com")
result = course.isalpha()
result = course.isdigit()
result = "contents".center(50, "*")
result = course.replace(" ", "-")
result = "Hello World".replace("World", "There")
result = course.split(" ")

print(result)
