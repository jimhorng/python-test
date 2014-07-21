
commit_log_file = "/Users/jimhorng/workspace/qcloud/api/commit.log"

f = open(commit_log_file, "r")
for line in f:
    tokens = line.split("\t")
    print(tokens[0])
    print(tokens[1])
    print(tokens[2])
    print(tokens[3])
    print(tokens[4])