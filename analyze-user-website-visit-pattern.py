from collections import defaultdict
from itertools import combinations

class Solution:
    def analyzeUserWebsiteVisitPattern(self, username: list[str], timestamp: list[int], website: list[str]) -> list[str]:
        # 1. Group websites by user and sort them by timestamp
        users_map = defaultdict(list)
        for user, time, site in zip(username, timestamp, website):
            users_map[user].append((time, site))
            
        patterns_count = defaultdict(int)
        
        for user in users_map:
            # Sort by timestamp
            users_map[user].sort()
            # Extract just the website names in chronological order
            sites = [site for time, site in users_map[user]]
            
            # 2. Get all unique 3-sequences for THIS user
            # We use a set because a user visiting the same 3-sequence 
            # multiple times only counts as 1 for that user.
            user_patterns = set(combinations(sites, 3))
            
            for pattern in user_patterns:
                patterns_count[pattern] += 1
                
        # 3. Find the pattern with max frequency, then sort lexicographically
        # Sorting by (-count, pattern) handles max count first, then alphabetical order
        result = sorted(patterns_count.items(), key=lambda x: (-x[1], x[0]))
        
        return list(result[0][0])