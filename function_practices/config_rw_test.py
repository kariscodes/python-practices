import configparser

config = configparser.ConfigParser()

TEST_CASE = 'read_config_file'
# TEST_CASE = 'write_config_file'


# read config file
if TEST_CASE == 'read_config_file':
    config.read('config.ini')
    config.sections()
    host = config['prod_database']['host']
    user = config['prod_database']['username']
    password = config['prod_database']['password']
    database = config['prod_database']['database']
    charset = config['prod_database']['characterset']
    appStyle = config['window_style']['application_style']
    font = config['window_style']['font']
    multiWindow = config['main_default']['multi_window_style']
    # three getter method: getint, getboolean, getfloat
    # logViewer = config['main_default']['show_log_viewer']               # return String
    logViewer = config['main_default'].getboolean('show_log_viewer')    # return Boolean
    print(host, user, password, database, charset)
    print(appStyle, font, multiWindow)
    print(logViewer, type(logViewer))

# write config file
if TEST_CASE == 'write_config_file':
    # writing method 1
    config['prod_database'] = {}
    config['prod_database']['host'] = '34.82.158.37'
    config['prod_database']['username'] = 'dev1'
    config['prod_database']['password'] = 'dev2020'
    config['prod_database']['database'] = 'myasset'
    config['prod_database']['characterset'] = 'utf8'
    config['window_style'] = {}
    config['window_style']['application_style'] = 'Fusion'
    config['window_style']['font'] = 'Times New Roman'
    # writing method 2
    config['main_default'] = {
            'multi_window_style' : 'tile',
            'show_log_viewer' : True
    }
    with open('../../ITRM-CS/config.ini', 'w') as configfile:
        config.write(configfile)        # clear file and rewrite