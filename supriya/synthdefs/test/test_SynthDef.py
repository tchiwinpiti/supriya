def test_SynthDef_01():

    a = 'SynthDef(\foo, { Out.ar(0, SinOsc.ar(freq:420) + SinOsc.ar(freq:440))'

    b = 'SCgf\x00\x00\x00\x02\x00\x01\x03foo\x00\x00\x00\x03C' + \
        '\xd2\x00\x00\x00\x00\x00\x00C\xdc\x00\x00\x00\x00\x00\x00' + \
        '\x00\x00\x00\x00\x00\x00\x00\x04\x06SinOsc\x02\x00\x00\x00' + \
        '\x02\x00\x00\x00\x01\x00\x00\xff\xff\xff\xff\x00\x00\x00\x00' + \
        '\xff\xff\xff\xff\x00\x00\x00\x01\x02\x06SinOsc\x02\x00\x00' + \
        '\x00\x02\x00\x00\x00\x01\x00\x00\xff\xff\xff\xff\x00\x00\x00' + \
        '\x02\xff\xff\xff\xff\x00\x00\x00\x01\x02\x0cBinaryOpUGen\x02' + \
        '\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00' + \
        '\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x02\x03Out\x02' + \
        '\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x00' + \
        '\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00'

