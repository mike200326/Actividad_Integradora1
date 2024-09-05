def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def contains_code(transmission, code):
    index = transmission.find(code)
    if index != -1:
        return f"true {index + 1}"
    else:
        return "false"

def find_longest_palindrome(s):
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

def longest_common_substring(trans1, trans2):
    n, m = len(trans1), len(trans2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    length, end_index = 0, 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if trans1[i - 1] == trans2[j - 1]:
                dp=dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > length:
                    length = dp[i][j]
                    end_index = i

def main():
    # Read the content from the files
    transmission1 = read_file('transmission1.txt')
    mcode1 = read_file('mcode1.txt')
    

    # Check if each malicious code is in the transmissions
    print(contains_code(transmission1, mcode1))
    
    # Find the longest palindromic substring in each transmission
    print(find_longest_palindrome(transmission1))
    

    # Find the longest common substring between the two transmissions
    print(longest_common_substring(transmission1))

if __name__ == "__main__":
    main()