# Script for importing csv files to plot2 with comments
open(IN,$file);
@descr = @array;
$line=0;
while(<IN>) {
    @column=split(',', $_);
    if($column[0] == "nr"){
        @descr = @column;
    }else{
        &log("Iterating data line $line\n");

        for $i (1 .. $#column){
            $data[$i-1][$line][0]=$column[0];
            $data[$i-1][$line][1]=$column[$i];
            $source[$i-1]="$file";
            $comment[$i-1]="$descr[$i]";
        }
        $line++;
    }
}
close(IN);
&log("$line number of points");
