#!/bin/bash

for FILE in $(find "./data/secret" -name "*.in"); do
        STEM=${FILE%%.in}

        VALPYTHON3=$( (/usr/bin/time -f "%e" python3 ./f.py < ${STEM}.in > ${STEM}.out ) 2>&1)
        VALPYPY=$( (/usr/bin/time -f "%e" pypy ./f.py < ${STEM}.in > ${STEM}.out ) 2>&1)

        # DIFF=$(diff ${STEM}.out ${STEM}.ans)

        echo "Testcase: $STEM"
        echo "Python3 took ${VALPYTHON3}"
        echo "pypy    took ${VALPYPY}"
        echo
done
