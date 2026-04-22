class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_log, digit_log = [], []

        for log in logs:
            val = log.split(' ')
            key, val = val[0], ' '.join(val[1:])
            
            if val[0].isdigit():
                digit_log.append(log)
            else:
                letter_log.append([val, key, log])

        letter_log = sorted(letter_log)
        letter_log = [log[2] for log in letter_log]
        return letter_log + digit_log