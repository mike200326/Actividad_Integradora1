def read_file(file_path: str) -> str:
    """
    Reads the content of a file and returns it as a string.
    
    :param file_path: Path to the file to be read.
    :return: Content of the file as a string.
    """
    with open(file_path, 'r') as file:
        return file.read()


def compute_lps(pattern: str) -> list:
    """
    Computes the longest prefix which is also a suffix (LPS) array for the KMP algorithm.
    
    :param pattern: The pattern string for which to compute the LPS array.
    :return: LPS array for the given pattern.
    """
    length = 0
    lps = [0] * len(pattern)
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def contains_code(transmission: str, code: str) -> str:
    """
    Checks if a malicious code is present in a transmission using the KMP algorithm.
    
    :param transmission: Transmission data as a string.
    :param code: Malicious code to search for in the transmission.
    :return: 'true <index>' if the code is found, 'false' otherwise.
    """
    m = len(code)
    n = len(transmission)
    
    lps = compute_lps(code)
    i = 0  # Index for transmission
    j = 0  # Index for code

    while i < n:
        if code[j] == transmission[i]:
            i += 1
            j += 1

        if j == m:
            return f"true {i - j + 1}"  # Found code at index (1-based)
        elif i < n and code[j] != transmission[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return "false"


def find_longest_palindrome(s: str) -> str:
    """
    Finds the longest palindromic substring in a given string.
    
    :param s: Input string.
    :return: Start and end positions (1-based) of the longest palindromic substring.
    """
    t = '#'.join('^{}$'.format(s))
    n = len(t)
    p = [0] * n
    center = right = 0

    for i in range(1, n - 1):
        if i < right:
            p[i] = min(right - i, p[2 * center - i])
        while t[i + p[i] + 1] == t[i - p[i] - 1]:
            p[i] += 1

        if i + p[i] > right:
            center, right = i, i + p[i]

    max_len = max(p)
    center_index = p.index(max_len)

    start = (center_index - max_len) // 2
    end = start + max_len

    return f"{start + 1} {end}"


def longest_common_substring(trans1: str, trans2: str) -> str:
    """
    Finds the longest common substring between two strings.
    
    :param trans1: First transmission string.
    :param trans2: Second transmission string.
    :return: Start and end positions (1-based) of the longest common substring in the first string.
    """
    n, m = len(trans1), len(trans2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    length, end_index = 0, 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if trans1[i - 1] == trans2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > length:
                    length = dp[i][j]
                    end_index = i

    start_index = end_index - length + 1
    return f"{start_index} {end_index}"


def main():
    # Use the corrected file names
    transmission1 = read_file('transmission1_content.txt')
    transmission2 = read_file('transmission2_content.txt')
    mcode1 = read_file('mcode1_content.txt')
    mcode2 = read_file('mcode2_content.txt')
    mcode3 = read_file('mcode3_content.txt')

    # Check if each malicious code is in the transmissions
    print(contains_code(transmission1, mcode1))
    print(contains_code(transmission1, mcode2))
    print(contains_code(transmission1, mcode3))
    print(contains_code(transmission2, mcode1))
    print(contains_code(transmission2, mcode2))
    print(contains_code(transmission2, mcode3))

    # Find the longest palindromic substring in each transmission
    print(find_longest_palindrome(transmission1))
    print(find_longest_palindrome(transmission2))

    # Find the longest common substring between the two transmissions
    print(longest_common_substring(transmission1, transmission2))


if __name__ == "__main__":
    main()
