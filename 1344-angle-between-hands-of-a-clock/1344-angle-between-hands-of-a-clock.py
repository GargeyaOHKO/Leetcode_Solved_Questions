class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        if hour==12: hourhand=((30/60)*minutes)
        else: hourhand=hour*30+((30/60)*minutes)
        minhand=(360/60)*minutes

        if hourhand<minhand:
            if minhand-hourhand<180:
                return minhand-hourhand
            else:
                return 360-(minhand-hourhand)
        elif minhand<hourhand:
            if hourhand-minhand<180:
                return hourhand-minhand
            else:
                return 360-(hourhand-minhand)
        else:
            return 0
