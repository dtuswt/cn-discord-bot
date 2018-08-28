class DtuUser:
    def __init__(self, study_id: str, password: str):
        self.study_id = study_id
        self.password = password
        self.secure_password = None
    
    # def __init__(self, study_id:str, secure_password: str):
    #     self.study_id = study_id
    #     self.password = None
    #     self.secure_password = secure_password
