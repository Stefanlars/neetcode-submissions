class Solution {
    fun hasDuplicate(nums: IntArray): Boolean {
        val hset: HashSet<Int> = HashSet<Int>()

        for (num in nums) {
            if (hset.contains(num)) {
                return true
            }

            hset.add(num)
        }

        return false
    }
}
