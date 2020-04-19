from pageProcess import TinderBot
from time import sleep
import sys

username = str(sys.argv[1])
password = str(sys.argv[2])
ideal_gr_ver = 1.854
ideal_gr_hor = 1.618

def main():
    bot = TinderBot()
    sleep(10)
    try:
        bot.login(username, password)
        print("Login Successful")
    except Exception as e:
        print("Login Failed")
        sleep(0.5)
        try:
            bot.alternateLogin(username, password)
            print("Alternate Login Successful")
        except Exception as exception:
            print("Alternate Login Failed")
            sleep(0.5)
            try:
                bot.login(username, password)
            except:
                sys.exit(1)


    sleep(10)

    try:
        bot.initTinder()
        while(True):
            golden_ratio_ver = []
            golden_ratio_hor = []

            for i in range(9):
                golden_ratio = bot.getGoldenRatioVariance()
                if(golden_ratio == None):
                    pass

                else:
                    golden_ratio_ver.append(golden_ratio[0])
                    golden_ratio_hor.append(golden_ratio[1])

                bot.nextImg()

            golden_ratio_isEmpty = ((not golden_ratio_ver) and (not golden_ratio_hor))



            if(golden_ratio_isEmpty):
                bot.sendRej()
            else:
                absolute_diff_ver = float(min(list(map(lambda x: abs(x - ideal_gr_ver), golden_ratio_ver))))
                absolute_diff_hor = float(min(list(map(lambda x: abs(x - ideal_gr_hor), golden_ratio_hor))))
                print("\nGolder Ratio Variance:\nHorizontal:{:.3f}\nVertical:{:.3f}".format(absolute_diff_hor, absolute_diff_ver))
                if((absolute_diff_ver < float(0.3)) or (absolute_diff_hor < float(0.3))):
                    bot.sendLike()
                    sleep(0.5)
                    if(bot.isOver()):
                        print("\n\nSwipes are Over.")
                        sys.exit(0)
                else:
                    bot.sendRej()
            sleep(0.5)

    except Exception as e:
        bot.closeHomeScreenPU()





if __name__ == '__main__':
    main()
