'''
Created on Apr 25, 2014

@author: alex
'''
import os
import stat
import fcntl
import gevent
import time

from errno import ENOENT, EAGAIN , EWOULDBLOCK
from gevent import socket
from socket import error

def set_close_exec(fd):
    flags = fcntl.fcntl(fd, fcntl.F_GETFD)
    fcntl.fcntl(fd, fcntl.F_SETFD, flags | fcntl.FD_CLOEXEC)

def bind_unix_socket(file, mode=0o600, backlog=128):
    """Creates a listening unix socket.

    If a socket with the given name already exists, it will be deleted.
    If any other file with that name exists, an exception will be
    raised.

    Returns a socket object (not a list of socket objects like
    `bind_sockets`)
    """
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    set_close_exec(sock.fileno())
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setblocking(0)
    try:
        st = os.stat(file)
    except OSError as err:
        if err.errno != ENOENT:
            raise
    else:
        if stat.S_ISSOCK(st.st_mode):
            os.remove(file)
        else:
            raise ValueError("File %s exists and is not a socket", file)
    sock.bind(file)
    os.chmod(file, mode)
    sock.listen(backlog)
    return sock

SOCK_HOME = '/Users/jimhorng/workspace/qcloud/tunnel/tmp'
bind_unix_socket(os.path.join(SOCK_HOME, 'qcloud_proxy.sock1'))
bind_unix_socket(os.path.join(SOCK_HOME, 'qcloud_internal_proxy.sock1'))
bind_unix_socket(os.path.join(SOCK_HOME, 'qcloud_ajax.sock1'))
