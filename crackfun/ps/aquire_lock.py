class Solution():
    def check_log_history(self,events):
        i = 0
        stack = []
        for i in range(len(events)):
            action, p = self.read_event(events[i])
            if action == 'ACQUIRE':
                stack.append(p)
            if action == 'RELEASE':
                if not stack:
                    return i+1
                oldp = stack.pop()
                if oldp!=p:
                    return i+1
        return [i+2,0][stack==[]]

    def read_event(self, event):
        action, p = event.split(' ')
        return action, p