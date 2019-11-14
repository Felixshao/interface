class base():

    def assert_Equal(self, first, two, msg=None):
        try:
            re = 'pass'
            if first == two:
                return re
            else:
                if msg is not None:
                    re = 'erron '
                    return re
                else:
                    re = 'erron!' + str(msg)
                    return re
        except BaseException as b:
            print(b)

            
print('123')


