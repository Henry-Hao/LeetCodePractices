/**
 * test
 */
import java.util.Arrays;
public class test {

    static int min = 1000;
    public static void main(String[] args) {
       int[][] data = new int[3][3];
       data[0] = new int[]{-2,-3,3};
       data[1] = new int[]{-5,-10,1};
       data[2] = new int[]{10,30,-5};
       System.out.println(calculateMinimumHP(data));
    }
    public static int calculateMinimumHP(int[][] dungeon) {
        helper(dungeon, 0, 0, 1000);
        return min + 1;
    }
    
    public static void helper(int[][] dungeon, int cur_x, int cur_y, int val){

        if(val <= 0)
            return;
        if(cur_x == dungeon.length - 1 && cur_y == dungeon[0].length - 1){
            int cost = 1000 - val - dungeon[cur_x][cur_y];
            if(cost < min && cost >= 0)
                min = cost;
            return;
        }
        
        int new_v = val + dungeon[cur_x][cur_y];
        // val += dungeon[cur_x][cur_y];
        if(cur_x < dungeon.length - 1)
            helper(dungeon, cur_x+1, cur_y, new_v);
        if(cur_y < dungeon[0].length - 1)
            helper(dungeon, cur_x, cur_y+1, new_v);
    }

}