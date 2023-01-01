import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    all_pages = corpus.keys()
    random_jump = (1 / len(all_pages)) * (1 - damping_factor)
    curr_link_to = corpus[page]
    link_to_prob = (
        0 if len(curr_link_to) == 0 else 1 / len(curr_link_to) * damping_factor
    )

    dist = {
        page: random_jump + link_to_prob if page in curr_link_to else random_jump
        for page in all_pages
    }

    return dist


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    assert n > 0
    sample_dist = {}
    curr_page = random.choice(list(corpus.keys()))
    for _ in range(n):
        model = transition_model(corpus, curr_page, damping_factor)
        pages = list(model.keys())
        page_weights = list(model.values())
        curr_page = random.choices(population=pages, weights=page_weights)[0]
        sample_dist[curr_page] = sample_dist.get(curr_page, 0) + 1

    dist_sample = {k: (v / n) for k, v in sample_dist.items()}
    return dist_sample


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    N = len(corpus.keys())

    dist = {p: 1 / N for p in corpus}
    flag = 0
    while True:
        for page in corpus:
            curr_prob = 0
            # this is the key, stack in here for a while.
            # have to ignore those not avalible for recursive calculation
            for linked_page in [p for p, linked in corpus.items() if page in linked]:
                curr_prob += dist[linked_page] / len(corpus[linked_page])

            curr_prob = (1 - damping_factor) / N + curr_prob * damping_factor

            # used all() before, but use flag inside loop more efficent
            if abs(dist[page] - curr_prob) < 0.001:
                flag += 1
            dist[page] = curr_prob

            if flag == N:
                return dist


if __name__ == "__main__":
    main()
