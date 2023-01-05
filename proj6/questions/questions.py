import nltk
import sys
import os
import string


FILE_MATCHES = 1
SENTENCE_MATCHES = 1


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    file_words = {filename: tokenize(files[filename]) for filename in files}
    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """
    dict = {}
    for file in os.listdir(directory):
        if ".txt" in file:
            file_path = os.path.join(directory, file)
            with open(file_path, "r") as f:
                content = f.read().replace("\n", "")
                dict[file] = content

    return dict


def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """
    return [
        t
        for t in nltk.tokenize.word_tokenize(document.lower())
        if not all(c in string.punctuation for c in t)
        and t not in nltk.corpus.stopwords.words("english")
    ]


def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """
    import math

    total_doc = len(documents)
    tokens = {}
    for sublist in documents.values():
        for t in sublist:
            if t not in tokens:
                appear = 0
                for doc_content in documents.values():
                    if t in doc_content:
                        appear += 1
                if appear == 0:
                    tokens[t] = 0
                else:
                    tokens[t] = math.log(total_doc / appear)

    return tokens


def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """
    res = {}
    for filename, content in files.items():
        score = 0
        for token in query:
            if token in content and token in idfs:
                score += content.count(token) * idfs[token]
        res[filename] = score

    ranked = sorted(res, key=res.get, reverse=True)
    return ranked[:n]


def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """
    res = {}
    for sen, words in sentences.items():
        score = 0
        count = 0
        for query_token in query:
            if query_token in words:
                count += 1
                score += idfs[query_token]
        res[sen] = (score, count / len(words))

    ranked = sorted(res, key=lambda k: (res[k][0], res[k][1]), reverse=True)[:n]
    return ranked


if __name__ == "__main__":
    main()
