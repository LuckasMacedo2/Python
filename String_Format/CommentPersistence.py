from CommentFormat import CommentFormat

class CommentPersistence:
    def __init__(self):
        self.file = 'objectBD.txt'
        self.objComment = CommentFormat()
    
    def saveObject(self):
        with open(self.file, 'w') as f:
            f.write(self.objComment.disassembleObject()) 
            f.close()

    def loadObject(self):
        with open(self.file, 'r') as f:
            self.objComment.assembleObject(f.read()) 
            f.close()
        
        return self.objComment