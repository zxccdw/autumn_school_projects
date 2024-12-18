class DbManager:
    def __init__(self, log):
        self.log = log
        self.log.info("DbManager init")
        
    def _connect(self):
        