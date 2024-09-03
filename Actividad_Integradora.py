def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def contains_code(transmission, code):
    index = transmission.find(code)
    if index != -1:
        return f"true {index + 1}"
    else:
        return "false"

def find_longest_palindrome(transmission):
    n = len(transmission)
    start, max_length = 0, 1

    for i in range(n):
        for j in range(i, n):
            substr = transmission[i:j+1]
            if substr == substr[::-1] and len(substr) > max_length:
                start = i
                max_length = len(substr)
    return f"{start + 1} {start + max_length}"

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