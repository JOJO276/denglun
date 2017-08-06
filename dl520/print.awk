BEGIN{OFS=" ";FS="----"}
{
   NF++;
   print $0
}

