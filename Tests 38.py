class Solution:
    def Solution(self):
        pass

    def nunberGame(self, remlist):
        addlist = []
        for time in range(0, int(len(remlist)/2)):
            min1 = remlist.pop(remlist.index(min(remlist)))
            print(f"Alice pick {min1}")
            min2 = remlist.pop(remlist.index(min(remlist)))
            print(f"Bob pick {min2}")
            addlist.append(min2)
            print(f"Bob add {min2}")
            addlist.append(min1)
            print(f"Alice add {min1}")

        print(addlist)


if __name__ == '__main__':
    obj = Solution()
    obj.nunberGame([10, 3, 2, 9])
