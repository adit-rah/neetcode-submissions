class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = {timestamp:value}
        else:
            self.store[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        mine = 1e9
        minv = ""
        for k,v in self.store[key].items():
            diff = timestamp - k
            if mine > diff and diff >= 0:
                mine = diff
                minv = v
        
        return minv
        
