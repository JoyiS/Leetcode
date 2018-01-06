class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        hh,mm = self.timeparser(time)
        digiset = set()
        for k in [mm%10, int(mm/10), hh%10, int(hh/10)]:
            digiset.add(k)
        val = hh*60+mm
        while True:
            val = val + 1
            hh = int(val/60) if int(val/60)<24 else int(val/60)-24
            mm = val%60
            newset = set()
            for k in [mm%10, int(mm/10), hh%10, int(hh/10)]:
                newset.add(k)
            if newset <= digiset:
                if hh<10:
                    hh = '0'+str(hh)
                if mm<10:
                    mm = '0'+str(mm)
                return str(hh)+':'+str(mm)

    def timeparser(self,time):
        hh = int(time[:2])
        mm = int(time[3:])
        return hh, mm

