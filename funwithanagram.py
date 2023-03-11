from typing import List


def funwithanagram(text: List) -> List:

    for i in range(len(text)):
        j = i + 1
        while j in range(len(text)):
            if sorted(text[i]) == sorted(text[j]):
                text.pop(j)
            else:
                j += 1
    text.sort()


if __name__ == '__main__':
    # text = ['code', 'doce', 'ecod', 'framer', 'frame']
    text = ['code', 'doce', 'ecod', 'cdeo', 'dcoe']
    text = ["geeks", "keegs","code", "doce"]
    funwithanagram(text)
    print(text)
