def decorate_report(func):
    def wrapper(*args, **kwargs):
        print("***************")
        func(*args, **kwargs)
        print("***************")
    return wrapper


class Report:
    template = "Default Template"

    
    def __init__(self, title, content):
        self.title = title
        self.content = content

    
    @classmethod
    def change_template(cls, new_template):
        cls.template = new_template

    
    def __str__(self):
        return (
            f"Name : {self.template}\n"
            f"Class   : {self.title}\n"
            f"Contact  : {self.content}"
        )

    
    @decorate_report
    def show_report(self):
        print(self)



Report.change_template("Rohit")

r1 = Report(
    "SY 11",
    "9168****15 "
)

r1.show_report()