from datetime import date

def sayHello(name):
    print(f"Hello, {name}!")

sayHello("VS Code")

def say_day_of_week(date):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[date.weekday()]

print(say_day_of_week(date.today()))