mvn package
for i in {1..}; do
  echo "exit" | java -jar ./target/PSTL_poker-1.0-SNAPSHOT.jar > testX0.txt
  python3 ./test.py < testX0.txt
  if [ $? -eq 1 ]; then
    echo "X0 invalide"
  else
    echo "X0 OK"
  fi
done
