import java.util.*;
class Solution {
	public static void main(String args[]){
		Scanner sc=new Scanner(System.in);
	}
    public int[] twoSum(int[] nums, int target) {
        for(int i=0;i<nums.lenght;i++){
            int a=target-nums[i];
            for (int j=nums.length-1;nums[j]>=a;j--){
                if (nums[j]==a){
                    return [i,j];
                }
            }
            return [-1,-1];
        }
    }
}
