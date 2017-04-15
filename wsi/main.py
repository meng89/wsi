
def find_module(app):




def install(softs):
    for sm in soft_modules:
        if hasattr(sm, 'is_installed'):
            if sm.is_installed():
                continue





def main():
    pass


if __name__ == '__main__':
    main()
