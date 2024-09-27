class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search_with_actions(self, query):
        node = self.root
        total_actions = 0

        for i, char in enumerate(query):
            total_actions += 1

            if char in node.children:
                node = node.children[char]
                if node.is_end_of_word:
                    return total_actions
            else:
                break

        total_actions += len(query) - len(query[:i + 1])
        return total_actions


def count_actions(database, queries):
    trie = Trie()

    for word in database:
        trie.insert(word)

    results = []

    for query in queries:
        actions = trie.search_with_actions(query)
        results.append(actions)

    return results


with open('input.txt', 'r', encoding='utf-8') as file_1:
    with open('output.txt', 'w', encoding='utf-8') as file_2:
        N = int(file_1.readline())
        database = [file_1.readline().strip() for _ in range(N)]
        Q = int(file_1.readline())
        queries = [file_1.readline().strip() for _ in range(Q)]

        results = count_actions(database, queries)

        for result in results:
            file_2.write(str(result) + '\n')
