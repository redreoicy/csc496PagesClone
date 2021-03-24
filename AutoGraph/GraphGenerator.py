import os
import pandas as pd
import re
import matplotlib.pyplot as plt

for subdir, dirs, files in os.walk(os.path.dirname(os.path.realpath(__file__))): #DO NOT USE os.getcwd() FOR DIRECTORY OF SCRIPT
    for filename in files:
        filepath = subdir + os.sep + filename


        if filepath.endswith("Benchmark.txt"): #currently only using the benchmark text files
            f = open(filepath, "r")
            data = []
            myx_ticks = []
            line = f.readline()
            currentGame = re.split(" ", line)[2].strip()[0:-4] #first game, remove the .exe
            game = ""
            while line != "":
                if line != "\n":
                    dataEntry = []
                    x = re.split(" ", line)
                    game = x[2].strip()[0:-4]
                    if game != currentGame:
                        # process the last game of data
                        df = pd.DataFrame(data, columns=['GPU Settings', 'Average framerate', 'Minimum framerate',
                                                         'Maximum framerate',
                                                         '1% low framerate', '0.1% low framerate'])
                        df['Average framerate'] = pd.to_numeric(df['Average framerate'])
                        df['Minimum framerate'] = pd.to_numeric(df['Minimum framerate'])
                        df['Maximum framerate'] = pd.to_numeric(df['Maximum framerate'])
                        df['1% low framerate'] = pd.to_numeric(df['1% low framerate'])
                        df['0.1% low framerate'] = pd.to_numeric(df['0.1% low framerate'])
                        df['GPU Settings'] = pd
                        prettyPlot = df.plot(title=currentGame + ' (more framerate is better)', xticks=df.index)
                        prettyPlot.set_xticklabels(myx_ticks)
                        plt.savefig(subdir + os.sep + currentGame+ '.png')
                        # to do add more stuff
                        data = []  # clear data for the next game
                        myx_ticks = []  # and ticks
                        currentGame = game;
                        ##process over

                    gpu = x[-2] + ' ' + x[-1].strip()
                    dataEntry.append(gpu) #add the gpu type
                    myx_ticks.append(gpu) #add the gpu to the ticks list
                    line = f.readline()
                    dataEntry.append(re.split(" ", line)[-2])  # add the average frames
                    line = f.readline()
                    dataEntry.append(re.split(" ", line)[-2])  # add the min frames
                    line = f.readline()
                    dataEntry.append(re.split(" ", line)[-2])  # add the max frames
                    line = f.readline()
                    dataEntry.append(re.split(" ", line)[-2])  # add the 1% frames
                    line = f.readline()
                    dataEntry.append(re.split(" ", line)[-2])  # add the 0.1% frames
                    data.append(dataEntry)

                line = f.readline()

            # process the last game of data
            df = pd.DataFrame(data, columns=['GPU Settings', 'Average framerate', 'Minimum framerate',
                                             'Maximum framerate',
                                             '1% low framerate', '0.1% low framerate'])
            df['Average framerate'] = pd.to_numeric(df['Average framerate'])
            df['Minimum framerate'] = pd.to_numeric(df['Minimum framerate'])
            df['Maximum framerate'] = pd.to_numeric(df['Maximum framerate'])
            df['1% low framerate'] = pd.to_numeric(df['1% low framerate'])
            df['0.1% low framerate'] = pd.to_numeric(df['0.1% low framerate'])
            df['GPU Settings'] = pd
            prettyPlot = df.plot(title=currentGame + ' (more framerate is better)', xticks=df.index)
            prettyPlot.set_xticklabels(myx_ticks)
            plt.savefig(subdir + os.sep + currentGame + '.png')
            # to do add more stuff
            data = []  # clear data for the next game
            myx_ticks = []  # and ticks
            currentGame = game;
            ##process over

            f.close()