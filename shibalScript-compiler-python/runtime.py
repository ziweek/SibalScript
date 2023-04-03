import sys



class ShibalScript:
    def __init__(self, path):
        path = self.path

    @staticmethod
    def type(code):
        if '씨발놈아!' in code:
            return 'START'
        if '봐라씨발' in code:
            return 'PRINT'
        if '아씨발' in code:
            return 'CONDITION'
        if '하씨발' in code:
            return 'REPEAT'
        if '수고해라!' in code:
            return 'END'
        if '씨발' in code:
            return 'DEF'


    def compileLine(self, code):
        if code == '':
            return None
        TYPE = self.type(code)
        
        if TYPE == 'DEF':
            res = code.replace("씨발 ","")
            return res
        elif TYPE == 'START':
            return ''
        elif TYPE == 'CONDITION':
            res = code.split("?")
            res = res.split("!")
            return res
        elif TYPE == 'PRINT':
            res = code.replace("봐라씨발","print")
            return res
        elif TYPE == 'END':
            return ''
        #     print(self.toNumber(code.split('화이팅!')[1]), end='')
        #     sys.exit()

    def compile(self, code):
        jun = False
        recode = ''
        spliter = '\n' if '\n' in code else '~'
        code = code.rstrip().split(spliter)
        # print(code)
        if (code[0].replace(" ","") != '씨발놈아!' or code[-1] != '수고해라!' ):
            raise SyntaxError('어떻게 이게 씨발스크립트냐!')
        index = 0
        error = 0
        container= []
        while index < len(code):
            errorline = index
            c = code[index].strip()
            # print(c)
            res = self.compileLine(c)
            container.append(res)
            # print(res)
            # print('---')
            if jun:
                jun = False
                code[index] = recode                
            if isinstance(res, int):
                index = res-2
            if isinstance(res, str):
                recode = code[index]
                code[index] = res
                index -= 1
                jun = True

            index += 1
            error += 1
            # if error == errors:
            #     raise RecursionError(str(errorline+1) + '번째 줄에서 무한 루프가 감지되었습니다.')
        f = open(self.path+"/result.py", 'w')
        for e in container:
            if type(e) == str:
                f.write(e)
                f.write('\n')
                # print(e)
        f.close()


    def compilePath(self, path):
        with open(path) as file:
            code = ''.join(file.readlines())
            self.compile(code)


if __name__ == '__main__':
    command = sys.argv[1]
    path = sys.argv[2]
    if command == 'build':
        ss = ShibalScript(path)
        ss.compilePath(path)
        