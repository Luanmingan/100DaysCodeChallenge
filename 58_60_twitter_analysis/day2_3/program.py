from wechat_api import Wechat


def main():
    wechat = Wechat()
    wechat.login(auto=True)

    wechat.plot_city()
    wechat.plot_gender()
    wechat.plot_province()
    wechat.word_cloud()


if __name__ == '__main__':
    main()
