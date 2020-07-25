class Question():
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self, answer):
        return self.answer == answer


# q1 = Question("en iyi programlama dili hangisidir?", [
#               "C#", "python", "java", "R"], "python")
# q2 = Question("en popüler programlama dili hangisidir?",
#               ["python", "C#", "java", "R"], "python")
# q3 = Question("en kazandıran programlama dili hangisidir?",
#               ["C#", "python", "java", "R"], "python")


# print(q1.checkAnswer("python"))
# print(q1.checkAnswer("C#"))

# Quiz


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 1

    def getQuestion(self):
        return self.questions[self.questionIndex]


q1 = Question("en iyi programlama dili hangisidir?", [
              "C#", "python", "java", "R"], "python")
q2 = Question("en popüler programlama dili hangisidir?",
              ["python", "C#", "java", "R"], "python")
q3 = Question("en kazandıran programlama dili hangisidir?",
              ["C#", "python", "java", "R"], "python")

questions = [q1, q2, q3]
quiz = Quiz(questions)
question = quiz.getQuestion()
print(question.text)
