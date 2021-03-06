
import time
import unittest
import subprocess
import dns.resolver

my_resolver = dns.resolver.Resolver(configure=False)
my_resolver.nameservers = ['127.0.0.1']

import shlex
class TestUnixSocket(unittest.TestCase):
    def test1_listening(self):
        """test listening unix socket"""
        cmd = 'su - _dnsdist -s /bin/bash -c \'python3 -c "from dnstap_receiver.receiver import start_receiver; start_receiver()" -u /var/run/dnsdist/dnstap.sock -v\''

        args = shlex.split(cmd)

        with subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) as proc:
            time.sleep(2)
            proc.terminate()
            
            o = proc.stdout.read()
            print(o)
        self.assertRegex(o, b"listening on /var/run/dnsdist/dnstap.sock")
        
    def test2_incoming_dnstap(self):
        """test to receive dnstap message"""
        cmd = 'su - _dnsdist -s /bin/bash -c \'python3 -c "from dnstap_receiver.receiver import start_receiver; start_receiver()" -u /var/run/dnsdist/dnstap.sock -v\''

        args = shlex.split(cmd)
        
        with subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) as proc:
            for i in range(10):
                r = my_resolver.resolve('www.github.com', 'a')
                time.sleep(1)

            proc.terminate()
            
            o = proc.stdout.read()
            print(o)
        self.assertRegex(o, b"dnsdist-unix CLIENT_RESPONSE")
        