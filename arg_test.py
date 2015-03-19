'''
Created on Mar 17, 2015

@author: jimhorng
'''

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(formatter_class = argparse.RawTextHelpFormatter)
    parser.add_argument('-u', '--unix_socket', dest = 'unix_socket', help = 'unix_socket which QCloud API listen to')
    parser.add_argument('-t', '--cpython', action='store_true')
    args = parser.parse_args()
    print "args.unix_socket: ", args.unix_socket
    print "args.cpython: ", args.cpython