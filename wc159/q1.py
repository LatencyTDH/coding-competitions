def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        prev = None
        offset = None
        n = len(coordinates)
        i = 1
        while i + 1 < n:
            a = coordinates[i-1]
            b = coordinates[i]
            c = coordinates[i+1]
            diff = b[0] - a[0], b[1] - a[1]
            diff2 = c[0] - a[0], c[1] - a[1]
            if diff[0] * diff2[1] - (diff[1] * diff2[0]) != 0:
                return False
            i += 1
        
        return True
      
if __name__ == '__main__':
	main()