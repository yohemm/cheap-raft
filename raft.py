import build
class Raft:
    def __init__(self, position:list = [0,0], build:str=''):
        self.position = position #(0,0) le centre
        self.build = None
        if not build == '':
            self.build = self.createBuild(build)

    def createBuild(self, buildName):
        return build.Build(buildName)
