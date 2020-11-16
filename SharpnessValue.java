public class SharpnessValue {

    public int findSharpnessValue(int[][] matrix) {
        if(matrix==null || matrix.length<1 || matrix[0].length<1) return -1;

        int m = matrix.length, n = matrix[0].length;
        int[][] sharpness = new int[m][n];

        for(int i=0; i<m; i++) {
            sharpness[i][0] = matrix[i][0];
        }

        for(int j=1; j<n; j++) {
            for(int i=0; i<m; i++) {
              //find the max sharpness from the left, upper left, and lower left path
                int pathPrev = sharpness[i][j-1];
                if(i>0) {
                    pathPrev = Math.max(pathPrev, sharpness[i-1][j-1]);
                }
                if(i<m-1) {
                    pathPrev = Math.max(pathPrev, sharpness[i+1][j-1]);
                }

                sharpness[i][j] = Math.min(pathPrev, matrix[i][j]);
            }
        }

        int maxSharpness = Integer.MIN_VALUE;
        for(int i=0; i<m; i++) {
            maxSharpness = Math.max(maxSharpness, sharpness[i][n-1]);
        }

        return maxSharpness;

    }

    public static void main(String[] args) {
        int[][] matrix = {{1}, {2}, {3}};

        SharpnessValue solver = new SharpnessValue();
        assert solver.findSharpnessValue(matrix)==3;

        int[][] matrix2 = {{1,2,3}};
        assert solver.findSharpnessValue(matrix2)==1;

        int[][] matrix3 = {{3}};
        assert solver.findSharpnessValue(matrix3)==3;

        int[][] matrix4 = {{5,7,2},
                            {7,5,8},
                            {9,1,5}};
        System.out.println(solver.findSharpnessValue(matrix4));

    }
}
