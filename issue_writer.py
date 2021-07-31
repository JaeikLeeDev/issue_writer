# 1. issue data가 담긴 csv 파일의 이름은 issues.csv로 할 것
# 2. issue data는 순서대로 issue number, tracker, category, subject 4개의 필드만을 갖는다.
# 3. issues.csv는 release_writer와 같은 directory 내에 위치할 것
# 4. 프로그램을 실행하면 'release_draft.txt'가 생성된다.

import csv

read_file = open('issues.csv', 'r')
write_file = open('release_draft.txt', 'w')
file = csv.reader(read_file)

for line in file:
    if line[0] == '\ufeff#' or line[0] == '#':
        header = line
    else:
        issue = '(#{issue_no}) ({tracker}) ({category})\n-{subject}\n\n' \
        .format(issue_no = line[0], tracker = line[1], category = line[2], subject = line[3])
        write_file.write(issue)

read_file.close()
write_file.close()

