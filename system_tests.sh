EXEC=inventory_management.py
TMP_OUT=tests/tmp-output

for testname in {1..5..1}; do
  python3 $EXEC < tests/$testname-input.txt > $TMP_OUT
  if ! diff -qwB tests/$testname-output.txt $TMP_OUT &>/dev/null; then
    echo "Test $testname failed"
  else
    echo "Test $testname passed"
  fi
done
rm $TMP_OUT
