class BasePasswordManager:
    old_password=["adsj@1346","S!3pl!1earn"]

    def get_password(self):
        #method that returns the current password as a string.
        return self.old_password[-1]

    def is_correct(self,stringg):#that receives a string and returns a boolean
        if stringg == self.old_password[-1]:
            return True 
        else:
            return False 


class PasswordManager(BasePasswordManager):#This class inherits from BasePasswordManager
    
    def __init__(self):
        self.level_old=0
        self.level_new=0
        BasePasswordManager.__init__(self)
        
    def  get_level(self,string):
        self.password=string
        a,n,sp=0,0,0
        for i in self.password:
            if i.isalpha():
                a=a+1
            elif i.isdigit():
                n=n+1
            else:
                sp=sp+1      
        if len(self.password)== a:
            return  0
        if len(self.password) == a+n:
            return  1
        if len(self.password)== a+n+sp:
            return  2
        
    def set_password(self,stringg):
        juna_password=BasePasswordManager.get_password(self)
        self.level_new=self.get_level(stringg)
        self.level_old=self.get_level(juna_password)
        
        if self.level_new >= self.level_old and len(stringg): 
            self.old_password.append(stringg)
            print("New password sucessfully added and securitylevel",self.level_new)
        else:
            print("Password is weak and lower security level than past password")




