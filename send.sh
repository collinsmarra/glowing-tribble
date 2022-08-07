#!/bin/bash

for i in {1..23}
do
    echo $(curl -sk http://127.0.0.1:8000/posts/posts/$i/likes)
done;
