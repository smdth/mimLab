!/bin/sh

echo "getting point list"
list=$(python mainDraw.py)
echo "calculatig point"
p=$(python main.py 1 1)
p1=$(python main.py 0 0)
p1=$(python parser.py ${1})
p2=$(python main.py 1 1)
p2=$(python parser.py ${2})
echo $p1
echo $p2
#python inverse_kinematics.py "$p1"
#sleep 3
#python inverse_kinematics.py "$p2"
