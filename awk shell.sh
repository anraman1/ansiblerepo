 awk '
{
total=$3+$4+$5
avg=total/3
if ( avg >= 90 ) Grade="A" ;
else if ( avg >= 80 ) Grade="B";
else if ( avg >= 70 ) Grade="C" ;
else Grade="D" ;
print $0,">==",Grade; 
 }' student.marks



cat access.log|awk '{ if ($9 == 200) count+=1  }  END { if ( count > 40 ) print count}'

awk 'ORS=NR%2?"|":"\n"' student.makes
