import java.util.Scanner;

class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int h = sc.nextInt();
        int w = sc.nextInt();
        int[][] a = new int[h][w];
        int[] sumh = new int[h];
        int[] sumw = new int[w];

        int i, j;
        for (i = 0; i < h; i++) {
            for (j = 0; j < w; j++) {
                a[i][j] = sc.nextInt();
                sumh[i] += a[i][j];
                sumw[j] += a[i][j];
            }
        }

        StringBuilder sb = new StringBuilder();
        for (i = 0; i < h; i++) {
            for (j = 0; j < w; j++) {
                sb.append(sumh[i] + sumw[j] - a[i][j]).append(" ");
            }
            sb.append("\n");
        }
        System.out.println(sb.toString());
    }
}