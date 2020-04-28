// https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/531/week-4/3313/

class FirstUnique {

    LinkedHashSet<Integer> uniq = new LinkedHashSet<>();
    Set<Integer> notUniq = new HashSet<>();
    
    public FirstUnique(int[] nums) {
        for (int n: nums) {
            if (uniq.contains(n)) {
                uniq.remove(n);
                notUniq.add(n);
            } else if (!notUniq.contains(n)) {
                uniq.add(n);
            }
        }
    }
    
    public int showFirstUnique() {
        if (uniq.isEmpty()) {
            return -1;
        } else {
            return uniq.iterator().next();
        }
    }
    
    public void add(int value) {
        if (uniq.contains(value)) {
            uniq.remove(value);
            notUniq.add(value);
        } else if (!notUniq.contains(value)) {
            uniq.add(value);
        }
    }
}

/**
 * Your FirstUnique object will be instantiated and called as such:
 * FirstUnique obj = new FirstUnique(nums);
 * int param_1 = obj.showFirstUnique();
 * obj.add(value);
 */