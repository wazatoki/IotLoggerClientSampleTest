from datetime import datetime

class Log_data:
    version = 0
    dt = datetime.strptime('1900/1/1 0:0:0', '%Y/%m/%d %H:%M:%S')
    speed = -32000
    flow = -32000
    pven = -32000
    pint = -32000
    deltap = -32000
    part = -32000
    tven = -32000
    tart = -32000
    svo2 = -32000
    hct = -32000
    
    def get_Data(self):

        return {
            "version": self.version,
            "datetime": self.dt,
            "speed": self.speed,
            "flow": self.flow,
            "pven": self.pven,
            "pint": self.pint,
            "deltap": self.deltap,
            "part": self.part,
            "tven": self.tven,
            "tart": self.tart,
            "svo2": self.svo2,
            "hct": self.hct,
        }