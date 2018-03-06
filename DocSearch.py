"""
Student No.: C1769331
"""
from tqdm import tqdm

def generateDictionary(docs):
    dictionary = []
    for doc in docs:
        for word in doc[0].split():
            dictionary.append(word)
    dictionary = set(dictionary)
    return dictionary


def generateInvertedIndex(dictionary, corpus):
    index = {}
    for word in dictionary:
        index[word] = []
    for doc in tqdm(corpus):
        for word in doc[0].split():
            # print(word)
            if word in index and doc[1] not in index[word]:
                index[word].append(doc[1])
    return index


def main():
    # Placeholders for data to be imported/generated
    docs = []
    queries = []

    # Load the corpus
    with open("./corpus/set2/docs.txt") as fp:
        docs = [(x.strip('\n'), i) for i, x in enumerate(fp.readlines(), 1)]

    # Load the queries
    with open("./corpus/set1/queries.txt") as fp:
        queries = [(x.strip('\n'), i) for i, x in enumerate(fp.readlines(), 1)]

    dictionary = generateDictionary(docs)
    invertedIndex = generateInvertedIndex(dictionary, docs)
    print(docs)
    print(queries)
    print(dictionary)
    print(invertedIndex)


if __name__ == "__main__":
    main()
