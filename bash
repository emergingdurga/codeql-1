if echo "$infraRef" | grep -q "_pre"; then
  echo "Pre"
else
  echo "Not Pre"
fi