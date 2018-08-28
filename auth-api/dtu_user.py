class DtuUser:
    def __init__(self, study_id: str, password: str, secure_password: str = None):
        self.study_id = study_id
        self.password = password
        self.secure_password = secure_password
    
    # def __init__(self, study_id: str, password = None, secure_password: str):
    #     self.study_id = study_id
    #     self.password = None
    #     self.secure_password = secure_password
