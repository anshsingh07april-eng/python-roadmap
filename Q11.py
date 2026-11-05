#Q11. Challenge: longest unique substring. Given a string, return the length of the longest substring with no repeating characters (for example, "abcabcbb" gives 3, "pwwkew" gives 3, "bbbbb" gives 1). Start with a brute-force version, then write a faster sliding-window version using a dictionary of last-seen positions.

def longest_unique_substring_brute_force(s):
    if not s:
        return 0

    max_length = 0
    n = len(s)

    for i in range(n):
        seen = set()
        for j in range(i, n):
            if s[j] in seen:
                break
            seen.add(s[j])
        max_length = max(max_length, len(seen))

    return max_length

def longest_unique_substring_sliding_window(s):
    if not s:
        return 0

    last_seen = {}
    max_length = 0
    start = 0

    for end, char in enumerate(s):
        if char in last_seen and last_seen[char] >= start:
            start = last_seen[char] + 1
        last_seen[char] = end
        max_length = max(max_length, end - start + 1)

    return max_length

# Test cases
print(longest_unique_substring_brute_force("abcabcbb"))  # 3
print(longest_unique_substring_brute_force("pwwkew"))    # 3
print(longest_unique_substring_brute_force("bbbbb"))     # 1

print(longest_unique_substring_sliding_window("abcabcbb"))  # 3
print(longest_unique_substring_sliding_window("pwwkew"))    # 3
print(longest_unique_substring_sliding_window("bbbbb"))     # 1