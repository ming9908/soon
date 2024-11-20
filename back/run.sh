#!/bin/sh
#!/bin/bash

cd back/

python3 -m uvicorn main:app --reload