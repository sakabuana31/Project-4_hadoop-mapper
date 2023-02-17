# from mrjob.job import MRJob

# class WordCountJob(MRJob):

#     def mapper(self, _, line):
#         for word in line.split():
#             yield word, 1

#     def reducer(self, word, counts):
#         yield word, sum(counts)

# if __name__ == '__main__':
#     WordCountJob.run()

import csv
from mrjob.job import MRJob

class WordCountJob(MRJob):

    def mapper(self, _, line):
        for word in line.split():
            yield word, 1

    def reducer(self, word, counts):
        yield None, (word, sum(counts))

    def reducer_final(self):
        with open('word_counts.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['word', 'count'])
            for _, (word, count) in self:
                writer.writerow([word, count])

if __name__ == '__main__':
    WordCountJob.run()