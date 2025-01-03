from collections import deque
ALPHABETS = 'abcdefghijklmnopqrstuvwxyz'

def word_ladder(begin_word, end_word, word_list):
    # Add the end word to the word list (in case it's not included)
    word_set = set(word_list)
    if end_word not in word_set:
        return []

    # BFS setup
    queue = deque([[begin_word]])
    visited = set()
    visited.add(begin_word)

    while queue:
        path = queue.popleft()
        current_word = path[-1]

        # If we reached the end word, return the path
        if current_word == end_word:
            return path

        # Generate all possible next words
        for i in range(len(current_word)):
            for c in ALPHABETS:
                next_word = current_word[:i] + c + current_word[i+1:]
                if next_word in word_set and next_word not in visited:
                    visited.add(next_word)
                    queue.append(path + [next_word])

    # If no path is found
    return []

# Example usage
begin_word = "hit"
end_word = "cog"
word_list = ["hot", "dot", "jog", "lot", "log", "cog"]

result = word_ladder(begin_word, end_word, word_list)
if result:
    print(f"Shortest transformation sequence: {' -> '.join(result)}")
else:
    print("No transformation sequence found.")
