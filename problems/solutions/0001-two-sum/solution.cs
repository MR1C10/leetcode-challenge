public class Solution {
    public int[] TwoSum(int[] nums, int target) 
    {
        Dictionary<int, int> mapa = new Dictionary<int, int>();

        for (int i = 0; i < nums.Length; i++)
        {
            int complemento = target - nums[i];
            if (mapa.ContainsKey(complemento))
            {
                return new int[] {mapa[complemento], i};
            }

            if (!mapa.ContainsKey(nums[i]))
            {
                mapa[nums[i]] = i;
            }
        }

        return null;
    }
}