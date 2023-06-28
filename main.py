from UI import main, test_main
# 版本管理，加了个后门方便调试
build = "debug"
if __name__ == '__main__':
    if build == "release":
        main()
    else:
        test_main()
