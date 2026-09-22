class Solution {
    fun isAnagram(s: String, t: String): Boolean {
        
        if (s.length != t.length) return false


        val (list_s, list_t) = Pair(MutableList(26) { 0 }, MutableList(26) { 0 })

        for (i in s.indices) {
            list_s[s[i] - 'a'] += 1
            list_t[t[i] - 'a'] += 1
        }

        return list_s == list_t
    }
}
