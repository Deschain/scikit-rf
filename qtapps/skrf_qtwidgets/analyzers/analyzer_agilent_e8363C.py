from skrf_qtwidgets.analyzers import keysight_pna


class Analyzer(keysight_pna.Analyzer):
    DEFAULT_VISA_ADDRESS = "TCPIP0::192.168.1.50::5025::SOCKET"
    NAME = "Agilent E8363C"
    NPORTS = 2
    NCHANNELS = 32
    SCPI_VERSION_TESTED = 'A.09.80.20'
