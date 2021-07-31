# 1. issue data가 담긴 csv 파일의 이름은 issues.csv로 할 것
# 2. issues.csv는 issue_writer.py와 같은 directory 내에 위치할 것
# 3. 프로그램을 실행하면 'release_draft.txt'가 생성된다.

import csv

read_file = open('issues.csv', 'r')
write_file = open('release_draft.txt', 'w')
file = csv.reader(read_file)

columns = {}
for line in file:
    # The first row of the issue.csv
    if line[0] == '\ufeff#' or line[0] == '#':
        count = 0
        for column in line:
            columns[column] = count
            count+=1
    else:
        issue = '(#{issue_no}) ({tracker}) ({category})\n-{subject}\n\n<description>\n-{description}\n<last note>\n-{last_notes}\n\n' \
        .format(issue_no    = line[columns['\ufeff#']], \
                tracker     = line[columns['Tracker']], \
                category    = line[columns['Category']], \
                subject     = line[columns['Subject']], \
                description = line[columns['Description']], \
                last_notes  = line[columns['Last notes']])
        write_file.write(issue)

read_file.close()
write_file.close()

