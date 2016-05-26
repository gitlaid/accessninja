from ipaddr import IPNetwork

class Rule(object):

    def __init__(self):
        self._policy = None
        self._protocol = None
        self._src = None
        self._srcport = None
        self._dst = None
        self._dstport = None
        self._stateful = None
        self._expire = None
        self._log = None

    @property
    def policy(self):
        return self._policy

    @policy.setter
    def policy(self, value):
        if not value in ['allow', 'deny']: raise Exception("policy should be either 'allow' or 'deny'")
        self._policy = value

    @property
    def protocol(self):
        return self._protocol

    @protocol.setter
    def protocol(self, value):
        if not value in ['tcp', 'udp', 'tcpudp', 'any']: raise Exception("protocol must be either 'tcp', 'udp', 'tcpudp' or 'any'")
        self._protocol = value

    @property
    def src(self):
        return self._src

    @src.setter
    def src(self, value):
        if value is None:
            return
        # TODO IP validation
        self._src = value

    @property
    def srcport(self):
        return self._srcport

    @srcport.setter
    def srcport(self, value):
        if value is None:
            return
        # TODO IP validation
        self._srcport = value

    @property
    def dst(self):
        return self._dst

    @dst.setter
    def dst(self, value):
        if value is None:
            return
        # TODO IP validation
        self._dst = value

    @property
    def dstport(self):
        return self._dstport

    @dstport.setter
    def dstport(self, value):
        self._dstport = value

    @property
    def stateful(self):
        return self._stateful

    @stateful.setter
    def stateful(self, value):
        self._stateful = value

    @property
    def expire(self):
        return self._expire

    @expire.setter
    def expire(self, value):
        self._expire = value

    @property
    def log(self):
        return self._log

    @log.setter
    def log(self, value):
        self._log = value

    def __str__(self):
        return "RULE: POL:{} PROTO:{} SRC:{} PORT:{} DST:{} PORT:{} STATE:{} EXPIRE:{} LOG:{}".format(self._policy, self._protocol, self._src, self._srcport, self._dst, self._dstport, self._stateful, self._expire, self._log)

    def __repr__(self):
        return "Ruleset"

class ICMPRule(object):

    def __init__(self):
        self._policy = None
        self._protocol = None
        self._icmptype = None
        self._src = None
        self._dst = None
        self._expire = None
        self._log = None

    @property
    def policy(self):
        return self._policy

    @policy.setter
    def policy(self, value):
        if not value in ['allow', 'deny']: raise Exception("policy should be either 'allow' or 'deny'")
        self._policy = value

    @property
    def protocol(self):
        return self._protocol

    @protocol.setter
    def protocol(self, value):
        if not value in ['icmp']: raise Exception("protocol must be 'icmp'")
        self._protocol = value

    @property
    def icmptype(self):
        return self._icmptype

    @icmptype.setter
    def icmptype(self, value):
        self._icmptype = value

    @property
    def src(self):
        return self._src

    @src.setter
    def src(self, value):
        self._src = value

    @property
    def dst(self):
        return self._dst

    @dst.setter
    def dst(self, value):
        self._dst = value

    @property
    def expire(self):
        return self._expire

    @expire.setter
    def expire(self, value):
        self._expire = value

    @property
    def log(self):
        return self._log

    @log.setter
    def log(self, value):
        self._log = value

    def __str__(self):
        return "ICMP RULE: POL:{} PROTO:{} TYPE: {} SRC:{} DST:{} EXPIRE:{} LOG:{}".format(self._policy, self._protocol, self._icmptype, self._src, self._dst, self._expire, self._log)

    def __repr__(self):
        return "Ruleset"