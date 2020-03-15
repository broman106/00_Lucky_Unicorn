
def statement_decorator(statement, decoration):
    print(decoration * len(statement))
    print(statement)
    print(decoration * len(statement))
    return ""

feedback = "*** Yay a unicorn ****"
decoration = "*"

statement_decorator(feedback, decoration)
print()
statement_decorator("!! Sorry you lose !!", "!")
