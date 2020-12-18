# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
current = []
voltage = []
percentage =[]


def Battery_data_analysis():
    file_name = input("please enter the log file name(To open the default file, press Enter): ")
    if (len(file_name) == 0):
        file_name = "battery.txt"
        print(file_name)

    try:
        with open(file_name, "r",) as f:
            data = f.readlines()
            for line in data:
                s = line.split(":")
                if len(s) == 2:
                    a,b= s[0].strip(),s[1].strip()
                    if a == "current":
                        current.append(float(b))
                    if a == "voltage":
                        voltage.append(float(b))
                    if a == "percentage":
                        percentage.append(float(b))
        f.close()
    except:
        print(
            "File %s does not exist." % file_name)
        quit()


def pic(fig_1, fig_2, fig_3):
    fig = plt.figure("battery")
    plt.plot(fig_1, 'g--o', label="current")
    plt.plot(fig_2, 'r--*', label="voltage")
    plt.plot(fig_3, 'm:+', label="percentage")
    plt.title("battery data")
    plt.legend()
    plt.xlabel('')
    plt.ylabel('')
    plt.grid(True)
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Battery_data_analysis()
    pic(current, voltage, percentage)




