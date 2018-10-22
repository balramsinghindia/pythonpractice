from src.logexception.logframework import CustomUserException
import logging
LOG_FILENAME = 'example.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)

# Error & Exception handling

def parse_csv_and_get_columns(filename):
    count = 0

    if (filename) :
        logging.critical('first log')


    csvFile = open(filename, 'r')
    lines = csvFile.readlines()
    for line in lines[1:]:
        val = line.split(",")
        test_str_div = val[0] / val[11]
        print(test_str_div)
        test_zero_div = (int(val[0]) / int(val[11]))


if __name__ == "__main__":
    parse_csv_and_get_columns(filename="data/flights.csv")
