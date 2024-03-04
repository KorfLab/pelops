from subprocess import run
import sys

alignments = run(f'bl2seq -i reference -j {testgenes} -p blastn', shell=True, capture_output=True).stdout.decode().split('\n')
print(alignments[:-1])

