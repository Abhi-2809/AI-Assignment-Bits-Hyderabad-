from experta import *
label=0
class Greetings(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        yield Fact(action="greet")

    @Rule(Fact(action='greet'),
          NOT(Fact(a=W())))
    def func_1(self):
        self.declare(Fact(a=input("Are you interested in pursuing managerial work and Do you see yourself leading a team: ")))

    @Rule(Fact(action='greet'),
          NOT(Fact(b=W())))
    def func_2(self):
        self.declare(Fact(b=input("Are you passionate about programming to help in problem solving: ")))

    @Rule(Fact(action='greet'),
          NOT(Fact(c=W())))
    def func_3(self):
        self.declare(Fact(c=input("Is you cgpa above 8 : ")))

    @Rule(Fact(action='greet'),
          NOT(Fact(d=W())))
    def func_4(self):
        self.declare(Fact(d=input("Are you interested in conducting research to answer previously unsolved problems: ")))

    @Rule(Fact(action='greet'),
          NOT(Fact(e=W())))
    def func_5(self):
        self.declare(Fact(e=input("Are you inclined towards documenting your work for publication purposes: ")))

    @Rule(Fact(action='greet'),
          NOT(Fact(f=W())))
    def func_6(self):
        self.declare(Fact(f=input("In which sector do you have maximum accolades Management/IT/Research: ")))    




    @Rule(Fact(action='greet'),Fact(a="no"),Fact(b="no"),Fact(c="yes"),Fact(d="yes"),Fact(e="yes"),Fact(f="Research"))
    def greet(self):
        label=1
        print('\n')
        print("Great here is a list of course you can do for a career in Research: Research Methodology,Study/Lab/Design Oriented Projects")
        print('\n')
        print("You can be a part of these clubs to increase you exposure: IEEE,Spectrun,IPCD")

    Rule(Fact(action='greet'),Fact(a="no"),Fact(b="no"),Fact(c="no"),Fact(d="yes"),Fact(e="yes"),Fact(f="Research"))
    def greet_2(self):
        label=1
        print('\n')
        print("Great here is a list of course you can do for a career in Research: Research Methodology,Study/Lab/Design Oriented Projects")
        print('\n')
        print("You can be a part of these clubs to increase you exposure: IEEE,Spectrun,IPCD")     


    @Rule(Fact(action='greet'),Fact(a="yes"),Fact(b="no"),Fact(c="yes"),Fact(d="no"),Fact(e="no"),Fact(f="Management"))
    def greet_3(self):
        label=1
        print('\n')
        print("Great here is a list of course you can do for a career in Management: Principles of Management, Managerial Statistics")
        print('\n')
        print("You can be a part of these clubs to increase you exposure: Department of Management")

    Rule(Fact(action='greet'),Fact(a="yes"),Fact(b="no"),Fact(c="no"),Fact(d="no"),Fact(e="no"),Fact(f="Management"))
    def greet_4(self):
        label=1
        print('\n')
        print("Great here is a list of course you can do for a career in Management: Principles of Management, Managerial Statistics")
        print('\n')
        print("You can be a part of these clubs to increase you exposure: Department of Management")    


    @Rule(Fact(action='greet'),Fact(a="no"),Fact(b="yes"),Fact(c="yes"),Fact(d="no"),Fact(e="yes"),Fact(f="IT"))
    def greet_5(self):
        label=1
        print('\n')
        print("Great here is a list of course you can do for a career in IT: DSA,OOP,DMS,OS,Computer Networks")
        print('\n')
        print("You can be a part of these clubs to increase you exposure: CSA, CruX, ACM")

    Rule(Fact(action='greet'),Fact(a="no"),Fact(b="yes"),Fact(c="no"),Fact(d="no"),Fact(e="yes"),Fact(f="IT"))
    def greet_6(self):
        label=1
        print('\n')
        print("Great here is a list of course you can do for a career in IT: DSA,OOP,DMS,OS,Computer Networks")
        print('\n')
        print("You can be a part of these clubs to increase you exposure: CSA, CruX, ACM")    

    Rule(Fact(action='greet'),Fact(a="no"),Fact(b="yes"),Fact(c="yes"),Fact(d="no"),Fact(e="no"),Fact(f="IT"))
    def greet_7(self):
        label=1
        print('\n')
        print("Great here is a list of course you can do for a career in IT: DSA,OOP,DMS,OS,Computer Networks")
        print('\n')
        print("You can be a part of these clubs to increase you exposure: CSA, CruX, ACM")  

    Rule(Fact(action='greet'),Fact(a="no"),Fact(b="yes"),Fact(c="no"),Fact(d="no"),Fact(e="no"),Fact(f="IT"))
    def greet_8(self):
        label=1
        print('\n')
        print("Great here is a list of course you can do for a career in IT: DSA,OOP,DMS,OS,Computer Networks")
        print('\n')
        print("You can be a part of these clubs to increase you exposure: CSA, CruX, ACM")      


    

engine = Greetings()
engine.reset()  # Prepare the engine for the execution.
engine.run()  # Run it!

if(label==0):
    print("We could not find courses related to your interests, Please be more specific!!") 