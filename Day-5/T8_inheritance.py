class publisher:

    def title(self):
        self.t=input("Enter a title:")


class book(publisher):
    
    def member(self):
        self.mem=input("Member Name:")
        self.pg=input("Page no.")
        print("Member Name is ",self.mem)
        print("Page number is ",self.pg)

class tap(publisher):

    def play(self):
        self.p=input("Enter time of playing:")
        print("Time for playing is ",self.p)

a=book()
b=tap()
a.member()
b.play()        
