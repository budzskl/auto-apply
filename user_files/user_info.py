# User Info
# Below the use can implement each of their login infos for each website

class user_info:
    def __init__(self, resume, letter, pay_grade, locations, dis_status, vet_status, curr_date, race, hisp,):
        self.resume = resume
        self.letter = letter
        self.pay_grade = pay_grade
        self.locations = locations
        self.dis_status = dis_status
        self.vet_status = vet_status
        self.curr_date = curr_date
        self.race = race
        self.hisp = hisp

class login_info:
    def __init__(self, email, password):
        self.email = email
        self.password = password

class LinkedIn(login_info):
    def __init__(self, email, password):
        super().__init__(email, password)

class Indeed(login_info):
    def __init__(self, email, password):
        super().__init__(email, password)

class Handshake(login_info):
    def __init__(self, email, password):
        super().__init__(email, password)