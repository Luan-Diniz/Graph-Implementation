class Util:
    
    @staticmethod
    def convert_float(num):
        if type(num) == float and num.is_integer():
            return int(num)
        else:
            return num