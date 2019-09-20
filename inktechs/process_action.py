import getopt
import sys


class ProcessAction(object):

    def process_typical_arguments(self, args):
        # -c ./home/file.conf --o ./home/text.file       # sample run time argument

        try:
            opts, args = getopt.getopt(args, "c:o", ["config", "output="])
        except getopt.GetoptError as err:
            print("option not recognized")
            sys.exit()

        for o, a in opts:
            # print(opts)
            if o in ("-c", "--config"):
                Helper().set_configuration(a)

            if o in ("-o", "--output"):
                Helper().set_output(a)


class Helper:

    def set_configuration(self, a):
        print("\nUpdate configuration as following:", a)

    def set_output(self, a):
        print("\nGenerate output as following", a)

