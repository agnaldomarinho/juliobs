# -*-*- encoding: utf-8 -*-*-
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import xmlrpclib
import xmlrpc2scgi as xmlrpc
import sys


class Rtorrent:
    def __init__(self, host, porta="80", tipo="http"):
        if tipo == "http":
            self.s = xmlrpclib.ServerProxy('http://{}:{}'.format(host, porta))
        if tipo == "scgi":
            self.s = xmlrpc.RTorrentXMLRPCClient("scgi://{}:{}".format(host,
                porta))

    def get_up_rate(self):
        return self.s.get_upload_rate()

    def set_up_rate(self, rate):
        return self.s.set_upload_rate(rate)

    def get_down_rate(self):
        return self.s.get_download_rate()

    def set_down_rate(self, rate):
        return self.s.set_download_rate(rate)

 
@login_required
def torrents(request):
    errors = []
    try:
        #r = Rtorrent("casa.juliobs.com", "80", "http")
        r = Rtorrent("127.0.0.1", "5000", "scgi")

        if request.method == 'POST':
            if request.POST['up']:
                new_up = int(request.POST['up']) * 1024
                if new_up >= 30 * 1024 or new_up == 0:
                    r.set_up_rate(new_up)

            if request.POST['down']:
                new_down = int(request.POST['down']) * 1024
                r.set_down_rate(new_down)

        up = int(r.get_up_rate()) / 1024
        down = int(r.get_down_rate()) / 1024
        return render(request, 'torrents.html', {'up': up, 'down': down})
    except:
        errors.append(sys.exc_info())
        return render(request, 'torrents.html', {'errors': errors})
