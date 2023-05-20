import configparser

# 建立一個讀取 config 的 ConfigParser
config = configparser.ConfigParser()

# 讀取檔案，config.read_file 的輸入為文件指標
config.read_file(open("example.ini"))

fruit = config.get('DEFAULT', 'fruit')
print(fruit)